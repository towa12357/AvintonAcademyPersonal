# [Python Numpyチュートリアル](https://avinton.com/academy/python-numpy-tutorial-japanese/)
- Should describe the development environment and library versions

## Execution environment
- WSL Ubuntu20.04
- Visual Studio Code + "Remote - WSL" EXTENSION

## Problems and their solutions
__Problem1__
```
ImportError: cannot import name 'imread' from 'scipy.misc' (/home/[username]/.local/lib/python3.8/site-packages/scipy/misc/\_\_init\_\_.py)
```
__Solution__
```
# command
python3
>> import scipy
>> scipy.__version__

python3 -m pip install imageio
python3 -m pip install Pillow
```
__Reference__  
- [scipy.misc.imread](https://docs.scipy.org/doc/scipy-1.2.1/reference/generated/scipy.misc.imread.html)  
- [scipy.misc.imsave](https://docs.scipy.org/doc/scipy-1.2.1/reference/generated/scipy.misc.imsave.html)  
- [scipy.misc.imresize](https://docs.scipy.org/doc/scipy-1.2.1/reference/generated/scipy.misc.imresize.html)

__Problem2__
- Cannot Display graphical information on WSL2

__Solution__
- Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/)  
- Configure as follows especially
  - Display Number: "0"
  - Additional parameters for VcXsrv: "-ac -nowgl"
  - Fill the checkbox "Public Network"
```
# command
sudo apt install libgl1-mesa-dev xorg-dev

# /etc/resolv.conf
nameserver 172.30.16.1

# <.profile>
[+] export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0.0

# command
source ~/.profile
sudo apt-get install python3-tk
```

__Reference__
- [WSL2＋Ubuntu 20.04でGUIアプリを動かす](https://astherier.com/blog/2020/08/run-gui-apps-on-wsl2/)
- [WSL2のX-ServerでGUI表示する際に「export DISPLAY=:0.0」が効かない](https://blog.odaryo.com/2020/01/wsl2-xserver-export-display/)
- ["UserWarning: Matplotlib is currently using agg, ...](https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so)

## Content Reference
- Scipy
  - [Distance computations](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)