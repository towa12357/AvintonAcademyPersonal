# Import required libraries and modules
import fire
import glob
import numpy as np
import os

from PIL import Image 
from sklearn.decomposition import IncrementalPCA
from sklearn.cluster import KMeans

np.random.seed(0)

# Convert image data to numpy array
def img_to_matrix(img):
    img_array = np.asarray(img)
    return img_array

# Flatten numpy array
def flatten_img(img_array):
    s = img_array.shape[0] * img_array.shape[1] * img_array.shape[2]
    img_width = img_array.reshape(1, s)
    return img_width[0]

# First classification
def first_classification():

    # Create a list where each element is a path to an image
    img_paths = []
    for file in glob.glob("./images/*.jpg"):
        img_paths.append(file)

    # Obtain training data from image data
    dataset = []
    for i in img_paths:
        img = Image.open(i)
        # print(img.size)
        img = img.resize((int(1284/6), int(1828/6)), Image.BICUBIC)
        img = img_to_matrix(img)
        img = flatten_img(img)
        dataset.append(img)
    
    dataset = np.array(dataset)
    # print(dataset.shape)

    # Perform PCA for dimensionality reduction
    n = dataset.shape[0]
    batch_size = 100
    ipca = IncrementalPCA()
    
    for i in range(n//batch_size):
        r_dataset = ipca.partial_fit(dataset[i*batch_size:(i+1)*batch_size])

    r_dataset = ipca.transform(dataset)

    # Perform image classification by k-means clustering
    n_clusters = 4
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(r_dataset)
    labels = kmeans.labels_

    # Save images by classification
    for i in range(n_clusters):
        label = np.where(labels==i)[0]
    
        if not os.path.exists("sk-result/label"+str(i)):
            os.makedirs("sk-result/label"+str(i))
    
        for j in label:
            img = Image.open(img_paths[j])
            fname = img_paths[j].split('/')[-1]
            img.save("sk-result/label"+str(i)+"/"+fname)

# Second classification
def second_classification():
    poorly_classified_label_number = 0 
    path_to_poorly_classified_label = "./sk-results/label"+str(label_number)+"/"
    
    # Create a list where each element is a path to an image
    img_paths = []
    for root, dirs, files in os.walk(path_to_poorly_classified_label):
        for file in files:
            if file.endswith(".jpg"):
                img_paths.append(os.path.join(root, file))
    
    # Obtain training data from image data
    dataset = []
    for i in img_paths:
        img = Image.open(i)
        img = img.resize((int(1232/6), int(1754/6)), Image.BICUBIC)
        img = img_to_matrix(img)
        img = flatten_img(img)
        dataset.append(img)
    
    dataset = np.array(dataset)
    
    # Perform PCA for dimensionality reduction
    n = dataset.shape[0]
    batch_size = 100
    ipca = IncrementalPCA()
    
    for i in range(n//batch_size):
        r_dataset = ipca.partial_fit(dataset[i*batch_size:(i+1)*batch_size])
    
    r_dataset = ipca.transform(dataset)
    
    # Perform image classification by k-means clustering
    n_clusters = 6
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(r_dataset)
    labels = kmeans.labels_
    
    # Save images by classification
    for i in range(n_clusters):
        label = np.where(labels==i)[0]
    
        if not os.path.exists(path_to_poorly_classified_label+"label"+str(i)):
            os.makedirs(path_to_poorly_classified_label+"label"+str(i))
    
        for j in label:
            img = Image.open(img_paths[j])
            fname = img_paths[j].split('/')[-1]
            img.save(path_to_poorly_classified_label+"label"+str(i)+"/" + fname)
    
if __name__ == "__main__":
    fire.Fire({
        "1": first_classification,
        "2": second_classification,
        #"3": final_classification
    })