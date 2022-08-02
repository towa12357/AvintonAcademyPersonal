import cv2                                  # Read image
import fire                                 # Function-Commandoization
import glob                                 # Getting path-list for PDFs
import numpy as np                          # Convert data format and Processing array
import os
import pdf2image                            # PConvert PDF into data
from tensorflow.keras import layers, models # Make CNN
from tensorflow.keras.losses import SparseCategoricalCrossentropy # Loss function


# Get training data
## After execution, manually classify images to prepare training data
def get_training_data():
    DPI = 100                             # Dots per inch
    count = 0                             # Total number of pages
    os.makedirs("./train", exist_ok=True) # make directory for training
    os.makedirs("./train/text",)
    os.makedirs("./train/diagram",)
    os.makedirs("./train/image",)

    # Iteration for each PDF
    for i, pdf in enumerate(glob.glob("./PDFs/*.pdf")):
        pages = pdf2image.convert_from_path(pdf, DPI)

        # Iteration for each PDF page
        for j, page in enumerate(pages):
            page.save("./train/data_{:03d}.jpg".format(count+1))
            count += 1


# Construct and train CNN
def construct_and_train_cnn():
    count = 0                                 # Total number of pages
    images = np.empty((0, 0), dtype=np.int64) # image data
    labels = np.empty(0, dtype=np.int64)      # labels

    # Iteration for each Classification    
    for i, cls in enumerate(["text", "diagram", "image"]):
        
        # Iteration for each image data(=PDF page)
        for page in glob.glob("./train/" + cls + "/*.jpg"):
            
            # Read and process and labeling data for training
            image = cv2.resize(cv2.imread(page), (200, 140)) # Arguments up to 2 dimensions
            images = np .append(images, image)
            labels = np.append(labels, i)
            count = count + 1

    # Arrange training data
    images = np.reshape(images, (count, 200, 140, 3))

    # Construct CNN
    model = models.Sequential()
    
    # 2D convolutional layer
    model.add(layers.Conv2D(
        filters=81,                 # Dimensions of output space
        kernel_size=(2, 2),         # Folding window height and width
        activation="relu",          # Activation function
        input_shape=(200, 140, 3))) # Input space
    
    # 2D maxpooling layer
    model.add(layers.MaxPooling2D((2, 2))) # Application area size
    
    # 2D convolutinal layer
    model.add(layers.Conv2D(filters=243, kernel_size=(2, 2), activation="relu"))

    # 2D maxpooling layer
    model.add(layers.MaxPooling2D((2, 2)))

    # Flattening layer
    model.add(layers.Flatten())
    
    # Full-coupled layers
    model.add(layers.Dense(units=64, activation="relu"))
    model.add(layers.Dense(units=3, activation="softmax"))

    # configure training process
    model.compile(
        optimizer="adam",                                     # Optimizer
        loss=SparseCategoricalCrossentropy(from_logits=True), # Loss function
        metrics=['accuracy']                                  # Evaluation metrix
        )
 
    # Training and Preserve CNN    
    model.fit(x=images, y=labels, epochs=5)
    model.save("./model.h5")


# Evaluation CNN
def evaluation_cnn():
    
    count = 0                                 # Total number of pages
    images = np.empty((0, 0), dtype=np.int64) # Image data
    labels = np.empty(0, dtype=np.int64)      # Labels
    os.makedirs("./verify", exist_ok=True)    # make directory for verifying

    # Iteration for each Classification
    for i, cls in enumerate(["text", "diagram", "image"]):
    
        # Iteration for each image data(=PDF page)
        for page in glob.glob("./verify/" + cls + "/*.jpg"):
            
            # Read, process and labeling data for verification
            image = cv2.resize(cv2.imread(page), (200, 140))
            images = np.append(images, image)
            labels = np.append(labels, i)
            count = count + 1

    # Arrange verification data
    images = np.reshape(images, (count, 200, 140, 3))

    # Read and evaluate CNN model
    model = models.load_model("./model.h5")
    evaluate = model.evaluate(x=images, y=labels)


# Function-commandoization
if __name__ == "__main__":
    fire.Fire({"g": get_training_data, "c": construct_and_train_cnn, "e": evaluation_cnn})