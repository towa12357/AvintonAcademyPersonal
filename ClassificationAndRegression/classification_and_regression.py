import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier

center = [ [1.5, 0.5], [-2.0, -1.0], [0,0]] # Center coordinates of data generation
DSIZE = 20                                  # Number of points to be generated from the center point

# Generate points
data = [ c + (np.random.randn(DSIZE,2) / 2) for c in center]

# Stick three numpy arrays together
data = np.concatenate(data)

# Label each point with a label corresponding to the point from which it was generated
label = np.arange(3*DSIZE)//DSIZE
 
# for i in range(3):
#     plt.scatter(data[:,0][label==i],data[:,1][label==i])

# plt.show()

# Refression
X, y = np.split(data, 2, axis=1)

## Learning and Prediction
lr = LinearRegression().fit(X, y)
test_X = np.arange(-4, 5)
test_X = test_X.reshape(len(test_X), 1)
y_predict = lr.predict(test_X)
print(y_predict)

## Equation of the regression line
y_predict_function = lambda x: x * lr.coef_ + lr.intercept_
# print(y_predict_function(1.5))  # 0.5
# print(y_predict_function(-2.0)) # -1.0
# print(y_predict_function(0))    # 0

# plt.scatter(X, y, label="data")
# plt.plot(test_X, y_predict, label='linear model')
# plt.xlim(-4,4)
# plt.ylim(-4,4)
# plt.title("Predict result")
# plt.grid()
# plt.legend()
# plt.show()

# Classification
## Generate predictive models for KNN
neigh = KNeighborsClassifier().fit(data, label)

## Prediction 
### (2, 10) → (10, 2)
test_Xy = np.array([np.random.rand(10) * 6 - 3, np.random.rand(10) * 4 - 2]).T
predict_label = neigh.predict(test_Xy)
print(predict_label)

for i in range(3):
    rgb = [False for i in range(3)]
    rgb[i] = True
    plt.scatter(data[:,0][label==i],data[:,1][label==i], c=rgb)
    plt.scatter(test_Xy[:,0][predict_label==i], test_Xy[:,1][predict_label==i],c=rgb, marker="*", s=200)

plt.show()