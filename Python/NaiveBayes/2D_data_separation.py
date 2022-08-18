import matplotlib.pyplot as plt
import numpy as np

from sklearn.naive_bayes import GaussianNB

# traindata and label
x = np.array([[-2,6], [0,6], [0,7], [-2,5], [-3,3], [-1,0], [-2,0], [-3,1], [-1,4], [0,3], [0,1], [-1,7], [-3,5], [-4,3], [-2,0], [-3,7], [1,5], [1,2], [-2,3], [2,3], [-4,0], [-1,3], [1,1], [-2,2], [2,7], [-4,1]])
y = np.array([2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2])

# Combine coordinates and corresponding labels in a single column.
data = np.hstack((x, y.reshape(y.shape[0],1)))
data1 = data[np.where(data[:,2]==1)]
data2 = data[np.where(data[:,2]==2)]

# plt.close("all")
# plt.scatter(data1[:,0], data1[:,1], c="tab:blue")
# plt.scatter(data2[:,0], data2[:,1], c="tab:red")
# plt.show()

# Learning GaussianNB model
model = GaussianNB()
model.fit(x, y)

# testdata
test_data = np.array([[0,4], [1,0]])
 
# plt.close("all")
# plt.scatter(data1[:,0], data1[:,1], c="tab:blue")
# plt.scatter(data2[:,0], data2[:,1], c="tab:red")
# plt.scatter(test_data[:,0], test_data[:,1], c="k" )
# plt.show()

# Verification by test data
test_label = model.predict(test_data)
print("Label of test data", test_data[0], ":", test_label[0])
print("Label of test data", test_data[1], ":", test_label[1])