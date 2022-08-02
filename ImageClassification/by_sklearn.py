# 必要なライブラリ、モジュールのインポート
import os
import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
 
from sklearn.decomposition import IncrementalPCA
from sklearn.cluster import KMeans
 
np.random.seed(5)

# 何枚かの画像とそのサイズの表示
img_paths = []
## リストを作成するためのループ
for file in glob.glob("./1*/*.jpg"):
    img_paths.append(file)

# print("Image number:", len(img_paths))
# print("Image list make done.")
