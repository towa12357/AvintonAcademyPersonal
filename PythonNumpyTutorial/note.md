# [Python Numpyチュートリアル](https://avinton.com/academy/python-numpy-tutorial-japanese/)
- 「ブロードキャスト」、2つ目のコードの16行目のコメント内容が不完全("]"が足りない)
- 「Scipy」、「画像の操作」の内容を以下に修正
```
# import
from imageio.v2 import imread, imwrite
import numpy as np
from PIL import Image

# image readging
img = imread('assets/cat.jpg')

# image processing
g_tinted = img * [1, 0.95, 0.9]
img_tinted = np.array(Image.fromarray(g_tinted.astype(np.uint8)).resize((300, 300)))

# image writing
imwrite('assets/cat_tinted.jpg', img_tinted)
```
- 「Matplotlib」、「画像の表示」のimport文を以下に修正
```
import numpy as np
import matplotlib.pyplot as plt
from imageio.v2 import imread
```
- 開発環境やライブラリのバージョンについて記述しておくべき

## 実行環境
- WSL Ubuntu20.04
- Visual Studio Code + "Remote - WSL" EXTENSION

## 主なエラー内容および不都合
- ModuleNotFoundError: No module named 'numpy'
- As follows
1. ImportError: cannot import name 'imread' from 'scipy.misc' (/home/[username]/.local/lib/python3.8/site-packages/scipy/misc/\_\_init\_\_.py)
2. TypeError: Cannot handle this data type: (1, 1, 3), <f8
- As follows
1. Plot not displayed with no errors
2. python_numpy_tutorial.py:572: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.

## 上記に対する各対応
- Command "python3 -m pip install numpy"
- Mainly As follows
1. Command "python3", "import scipy" and "scipy.__version__"
2. Check [this](https://docs.scipy.org/doc/scipy-1.2.1/reference/generated/scipy.misc.imread.html)
3. Command "python3 -m pip install imageio"
4. Check [this](https://docs.scipy.org/doc/scipy-1.2.1/reference/generated/scipy.misc.imsave.html)
5. Check [this](https://docs.scipy.org/doc/scipy-1.2.1/reference/generated/scipy.misc.imresize.html)
6. Command "python3 -m pip install Pillow"
7. Check dtype and fix it

- Mainly as follows (Ref.[1-4](https://astherier.com/blog/2020/08/run-gui-apps-on-wsl2/#), [2.3](https://blog.odaryo.com/2020/01/wsl2-xserver-export-display/), [5](https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so))
1. Install [X server](https://sourceforge.net/projects/vcxsrv/)
2. Configure as follows especially 
  1. Display Number: "0"
  2. Additional parameters for VcXsrv: "-ac -nowgl"
  3. Fill the checkbox "Public Network"
3. Command "sudo apt install libgl1-mesa-dev xorg-dev"
4. In "~/.profile", add "export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0.0" 
5. Command "sudo apt-get install python3-tk"