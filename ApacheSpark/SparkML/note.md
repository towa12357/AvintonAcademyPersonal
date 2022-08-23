# [SparkMLによるKaggle Titanic生存者予測](https://avinton.com/academy/sparkml-kaggle-titanic-survivor-prediction/)
## Prerequisite
- [Apache SparkとApache Zeppelinの概要と環境構築](../EnvironmentBuilding/note.md)

## Procedure
- Download sample data
```
mkdir ~/zeppelin/data/titanic
cd ~/zeppelin/data/titanic
wget https://avinton.com/wp-content/uploads/2022/04/train.csv
wget https://avinton.com/wp-content/uploads/2022/04/test.csv
```
- Write codes At Zeppelin notebook
```
// import libraries
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml._
import org.apache.spark.ml.feature._
import org.apache.spark.ml.classification.RandomForestClassifier
import org.apache.spark.sql.functions._
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.types.IntegerType
import org.apache.spark.ml.tuning.ParamGridBuilder
import org.apache.spark.ml.param.ParamMap
import org.apache.spark.ml.tuning.CrossValidator
import org.apache.spark.ml.evaluation.BinaryClassificationEvaluator
import org.apache.spark.mllib.evaluation.MulticlassMetrics

// Read training data
val df = spark.read.option("header", "true").option("inferSchema", "true").csv("/data/titanic/train.csv")

// Check the data
// df.printSchema()
// df.show()
// df.groupBy("Sex").count().show()

// Deal with missing values (by filling mean value)
val meanValue = df.agg(mean(df("Age"))).first.getDouble(0)
val fixedDf = df.na.fill(meanValue, Array("Age"))

// Divide data
val dfs = fixedDf.randomSplit(Array(0.7, 0.3))
val trainDf = dfs(0).withColumnRenamed("Survived", "label")
val crossDf = dfs(1)

// Process categorical data
//// Create pipeline using one-hot encoding
def handleCategorical(column: String): Array[PipelineStage] = {
    val stringIndexer = new StringIndexer().setInputCol(column)
        .setOutputCol(s"${column}_index")
        .setHandleInvalid("skip")
    val oneHot = new OneHotEncoder().setInputCol(s"${column}_index").setOutputCol(s"${column}_onehot")
    Array(stringIndexer, oneHot)
}

//// Create stage for all category variables
val genderStages = handleCategorical("Sex")
val embarkedStages = handleCategorical("Embarked")
val pClassStages = handleCategorical("Pclass")

// Create a classifier using RandomForest
//// columns for training
val cols = Array("Sex_onehot", "Embarked_onehot", "Pclass_onehot", "SibSp", "Parch", "Age", "Fare")
val vectorAssembler = new VectorAssembler().setInputCols(cols).setOutputCol("features")

//// algorithm stage
val randomForestClassifier = new RandomForestClassifier()

//// pipeline
val preProcessStages = genderStages ++ embarkedStages ++ pClassStages ++ Array(vectorAssembler)
val pipeline = new Pipeline().setStages(preProcessStages ++ Array(randomForestClassifier))

// Fit model to training data
val model = pipeline.fit(trainDf)


// Score Calculation
def accuracyScore(df: DataFrame, label: String, predictCol: String) = {
    val rdd = df.select(label, predictCol).rdd.map(row => (row.getInt(0).toDouble, row.getDouble(1)))
    new MulticlassMetrics(rdd).accuracy
}

println("train accuracy with pipeline" + accuracyScore(model.transform(trainDf), "label", "prediction"))
println("train accuracy with pipeline" + accuracyScore(model.transform(crossDf), "Survived", "prediction"))

// result
train accuracy with pipeline0.8476499189627229
train accuracy with pipeline0.8161764705882353
```
```
// Define ParameterGrid
val paramMap = new ParamGridBuilder()
    .addGrid(randomForestClassifier.impurity, Array("gini", "entropy"))
    .addGrid(randomForestClassifier.maxDepth, Array(1,2,5,10,15))
    .addGrid(randomForestClassifier.minInstancesPerNode, Array(1,2,4,5,10))
    .build()

// Define Cross-Validation Stage
def crossValidation(pipeline: Pipeline, paramMap: Array[ParamMap], df: DataFrame): Model[_] = {
    val cv = new CrossValidator()
        .setEstimator(pipeline)
        .setEvaluator(new BinaryClassificationEvaluator)
        .setEstimatorParamMaps(paramMap)
        .setNumFolds(5)
    cv.fit(df)
}
val cvModel = crossValidation(pipeline, paramMap, trainDf)

// Calculate score again
println("train accuracy with pipeline" + accuracyScore(cvModel.transform(trainDf), "label", "prediction"))
println("train accuracy with pipeline" + accuracyScore(cvModel.transform(crossDf), "Survived", "prediction"))

// result
train accuracy with pipeline0.8346839546191248
train accuracy with pipeline0.8529411764705882
```
```
// Read and Process test data
val testDf = spark.read.option("header", "true").option("inferSchema", "true").csv("/data/titanic/test.csv")
val fareMeanValue = df.agg(mean(df("Fare"))).first.getDouble(0)
val fixedOutputDf = testDf.na.fill(meanValue, Array("age")).na.fill(fareMeanValue, Array("Fare"))

// Create Submit File
def generateOutputFile(testDF: DataFrame, model: Model[_]) = {
    val scoredDf = model.transform(testDF)
    val outputDf = scoredDf.select("PassengerId", "prediction")
    val castedDf = outputDf.select(outputDf("PassengerId"), outputDf("prediction").cast(IntegerType).as("Survived"))
    castedDf.write.format("csv").option("header", "true").mode(SaveMode.Overwrite).save("/data/titanic/output/")
}
generateOutputFile(fixedOutputDf, model)
```

## Review
- Error occurs when reading training data (SparkSession → spark)
- Error occurs when processing categorical data (s"{column}_index" → s"${column}_index") 
- Cross Validation took a long time to complete and there was no change in results
- Note that different models are used when recalculating scores