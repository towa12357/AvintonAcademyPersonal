import matplotlib.pyplot as plt
import numpy as np
import pandas as ps
from sklearn.ensemble import RandomForestClassifier as RandomForest
from sklearn.model_selection import train_test_split

# Data Reading
data = ps.read_csv('train.csv')

# Mapping Sex to Number
data['Gender'] = data['Sex'].map({"female": 0, "male": 1}).astype(int)

#Fill in NaN with the median
data["Age"] = data["Age"].fillna(data["Age"].median())

# Remove unnecessary elements
data = data.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)

# Separate elements and results
X = data.drop(['Survived', 'PassengerId'], axis=1).values
y = data['Survived'].values

# Separate 75% training data and 25% test data
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Predictive modeling
model = RandomForest(n_estimators=100).fit(X_train, y_train)

# Calculate the percentage of correct predictions
score = model.score(X_test, y_test)
print(score)

# Strength of the causal relationship of each element to the outcome
header = np.array(data.drop(['Survived', 'PassengerId'], axis=1).columns)
print(header)
print(model.feature_importances_)