# Import required libraries and modules
import fire
import matplotlib.pyplot as plt
import numpy as np

from imageio.v2 import imread, imwrite
from PIL import Image
from scipy.spatial.distance import pdist, squareform

def image_manipulation():

    # Image reading
    img_before = imread('images/cat_before.jpg')
    
    # Adjust the density of RGB    
    img_after = img_before * [1, 0.95, 0.9]

    # Resizing
    img_after = np.array(Image.fromarray(img_after.astype(np.uint8)).resize((300, 300)))

    # Image writing
    imwrite('images/cat_after.jpg', img_after)


def euclidean_distance():

    # Some points
    x = np.array([[0, 1], [1, 0], [2, 0]])
    
    # Euclidean distance between two points
    d = squareform(pdist(x, 'euclidean'))
    print(d)


def sine_and_cosine_plots(): 
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    plt.plot(x, y_sin)
    plt.plot(x, y_cos)
    plt.xlabel('x axis label')
    plt.ylabel('y axis label')
    plt.title('Sine and Cosine')
    plt.legend(['Sine', 'Cosine'])
    plt.show()


def sine_and_cosine_subplot(): 
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)    
    plt.subplot(2, 1, 1)
    plt.plot(x, y_sin)
    plt.title('Sine')
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')
    plt.show()

def image_subplot():
    # Image reading
    img_before = imread('images/cat_before.jpg')
    
    # Adjust the density of RGB    
    img_after = img_before * [1, 0.95, 0.9]
    
    plt.subplot(1, 2, 1)
    plt.imshow(img_before)
    plt.subplot(1, 2, 2)
    plt.imshow(np.uint8(img_after))
    plt.show()

if __name__ == "__main__":
    fire.Fire({
        "im": image_manipulation,
        "ed": euclidean_distance,
        "sacp": sine_and_cosine_plots,
        "sacs": sine_and_cosine_subplot,
        "is": image_subplot
    })