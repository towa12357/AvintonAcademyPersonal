def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
 
# print(quicksort([3,6,8,10,1,2,1]))
# "[1, 1, 2, 3, 6, 8, 10]" と表示

x = 3
# print(type(x)) # "<class 'int'>"と表示
# print(x) # "3"と表示
# print(x + 1) # 足し算; "4"と表示
# print(x - 1) # 引き算; "2"と表示
# print(x * 2) # 掛け算; "6"と表示
# print(x ** 2) # 累乗; "9"と表示
 
x += 1
# print(x) # "4"と表示
 
x *= 2
# print(x) # "8"と表示
 
y = 2.5
# print(type(y)) # "<class 'float'>"と表示
# print(y, y + 1, y * 2, y ** 2) # "2.5 3.5 5.0 6.25"と表示

t = True
f = False
# print(type(t)) # "<class 'bool'>"と表示
# print(t and f) # 論理AND; "False"と表示
# print(t or f) # 論理OR; "True"と表示
# print(not t) # 論理NOT; "False"と表示
# print(t != f) # 論理XOR; "True"と表示

hello = 'hello' # 文字列はシングル引用符で表示
world = "world" # もしくはダブル引用符で表示。どちらでも構わない
# print(hello) # "hello"と表示
# print(len(hello)) # 文字列の長さ; "5"と表示
 
hw = hello + ' ' + world # 文字列結合（もしくは連結）
# print(hw) # "hello world"と表示
 
hw12 = '%s %s %d' % (hello, world, 12) # C言語のsprintfに似た文字列フォーマット
# print(hw12) # "hello world 12"と表示

s = "hello" 
# print(s.capitalize()) # 先頭の文字を大文字にする; "Hello"と表示
# print(s.upper()) # 文字列全体を大文字にする; "HELLO"と表示
# print(s.rjust(7)) # 右揃えで、指定した文字数になるように空白を加える; " hello"と表示
# print(s.center(7)) # 中央揃えで、指定した文字数になるように空白を加える; " hello "と表示
# print(s.replace('l', '(ell)')) # 指定した文字列をすべて置換; "he(ell)(ell)o"と表示
# print(' world '.strip()) # 先頭と末尾から空白を削除; "world"と表示

xs = [3, 1, 2] # リストを作成
# print(xs, xs[2]) # "[3, 1, 2] 2"と表示
# print(xs[-1]) # 負の値ではリストの末尾から数える; "2"と表示
 
xs[2] = 'foo' # リストは異なったデータ型で構成できる
# print(xs) # "[3, 1, 'foo']"と表示
 
xs.append('bar') # 要素をリストの末尾に追加
# print(xs) # "[3, 1, 'foo', 'bar']"と表示
 
x = xs.pop() # リストの末尾の要素を削除し、引数として返す
# print(x, xs) # "bar [3, 1, 'foo']"と表示

nums = list(range(5)) # rangeは連続した数字を作り出す組み込み関数
# print(nums) # "[0, 1, 2, 3, 4]"表示
# print(nums[2:4]) # インデックス2から4（4は含めない）のリストを取得; "[2, 3]"と表示
# print(nums[2:]) # インデックス2から終わりまでのリストを取得; "[2, 3, 4]"と表示
# print(nums[:2]) # 初めからインデックス2（2は含めない）までのリストを取得; "[0, 1]"と表示
# print(nums[:]) # リストすべてを取得; "[0, 1, 2, 3, 4]"と表示
# print(nums[:-1]) # スライスには負の値も使用できる; "[0, 1, 2, 3]"と表示
 
nums[2:4] = [8, 9] # スライスで取り出した部分に新しいリストを割り当てる
# print(nums) # "[0, 1, 8, 9, 4]"と表示

animals = ['cat', 'dog', 'monkey']
# for animal in animals:
#     print(animal) 
      # "cat", "dog", "monkey"をそれぞれ別の行で表示

animals = ['cat', 'dog', 'monkey'] 
# for idx, animal in enumerate(animals):
#     print('#%d: %s' % (idx + 1, animal)) 
    # "#1: cat", "#2: dog", "#3: monkey"をそれぞれ別の行で表示

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
 
# print(squares) # "[0, 1, 4, 9, 16]"と表示

nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
# print(squares) # "[0, 1, 4, 9, 16]"と表示

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
# print(even_squares) # "[0, 4, 16]"と表示


d = {'cat': 'cute', 'dog': 'furry'} # データと共に、新しい辞書を作成
# print(d['cat']) # キーに対応する値を取り出す; "cute"と表示
# print('cat' in d) # 辞書が、与えられたキーを持つかどうかを確認; "True"と表示
 
d['fish'] = 'wet' # 辞書に要素を追加
# print(d['fish']) # "wet"と表示
# print(d['monkey']) # KeyError: 'monkey'はdの中に存在しない
# print(d.get('monkey', 'N/A')) # キーが存在しなければ"N/A"（指定しなければNone）を表示; "N/A"と表示
# print(d.get('fish', 'N/A')) # キーが存在すれば対応する値を表示; "wet"と表示

del d['fish'] # 辞書から要素を削除 
# print(d.get('fish', 'N/A')) # "fish" は削除されている; "N/A"と表示

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    # print('A %s has %d legs' % (animal, legs))
    # "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"と表示

d = {'person': 2, 'cat': 4, 'spider': 8}
# for animal, legs in d.items():
#     print('A %s has %d legs' % (animal, legs))
    # "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"と表示

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
# print(even_num_to_square) # "{0: 0, 2: 4, 4: 16}"と表示

animals = {'cat', 'dog'}
# print('cat' in animals) # 要素がセット内にあるかどうかを確認する; "True"と表示
# print('fish' in animals) # "False"と表示
 
animals.add('fish') # セットに要素を追加
# print('fish' in animals) # "True"と表示
# print(len(animals)) # セット内の要素の数; "3"と表示
 
animals.add('cat') # すでにセット内にある要素は追加しても何も変わらない
# print(len(animals)) # "3"と表示
 
animals.remove('cat') # セットから要素を削除
# print(len(animals)) # "2"と表示

animals = {'cat', 'dog', 'fish'}
# for idx, animal in enumerate(animals):
#     print('#%d: %s' % (idx + 1, animal))
    # "#1: fish", "#2: dog", "#3: cat"と表示（順序は実行のたびに変わります）

from math import sqrt 
nums = {int(sqrt(x)) for x in range(30)}
# print(nums) # "{0, 1, 2, 3, 4, 5}"と表示

d = {(x, x + 1): x for x in range(10)} # タプルをキーとして用いた辞書を作成
t = (5, 6) # タプルを作成
# print(type(t)) # "<class 'tuple'>"と表示
# print(d[t]) # "5"と表示
# print(d[(1, 2)]) # "1"と表示


def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'
 
# for x in [-1, 0, 1]:
#     print(sign(x))
# "negative", "zero", "positive"と表示


def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)
 
# hello('Bob') # "Hello, Bob"と表示
# hello('Fred', loud=True) # "HELLO, FRED!"と表示

class Greeter(object):
 
    # コンストラクタ
    def __init__(self, name):
        self.name = name # インスタンス変数を作成
 
    # インスタンスメソッド
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)
 
# g = Greeter('Fred') # Greeterクラスのインスタンスを生成
# g.greet() # インスタンスメソッドを呼び出す; "Hello, Fred"と表示
# g.greet(loud=True) # インスタンスメソッドを呼び出す; "HELLO, FRED!"と表示

import numpy as np

a = np.array([1, 2, 3]) # 階数1の配列を作成
# print(type(a)) # "<class 'numpy.ndarray'>"と表示
# print(a.shape) # "(3,)"と表示
# print(a[0], a[1], a[2]) # "1 2 3"と表示
 
a[0] = 5 # 配列の要素を変更
# print(a) # "[5 2 3]"と表示
 
b = np.array([[1,2,3],[4,5,6]]) # 階数2の配列を作成
# print(b.shape) # (2, 3)"と表示
# print(b[0, 0], b[0, 1], b[1, 0]) # "1 2 4"と表示

import numpy as np
 
a = np.zeros((2,2)) # すべて0の配列を作成
# print(a) # "[[ 0. 0.]
           # [ 0. 0.]]"と表示
 
b = np.ones((1,2)) # すべて1の配列を作成
# print(b) # "[[ 1. 1.]]"と表示
 
c = np.full((2,2), 7) # 任意の定数配列を作成
# print(c) # "[[ 7 7]
           # [ 7 7]]"と表示
 
d = np.eye(2) # 2x2の単位行列を作成
# print(d) # "[[ 1. 0.]
           # [ 0. 1.]]"と表示
 
e = np.random.random((2,2)) # 無作為な値の配列を作成
# print(e) # "[[ 0.91940167 0.08143941]
           # [ 0.68744134 0.87236687]]"と表示（一例）

import numpy as np

# 以下の、階数2、形状(3, 4)の配列を作成
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]] 
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) 

# スライスを用い、初めの2行と2,3列目を抽出
# bは以下の、形状(2, 2)の配列
# [[2 3]
# [6 7]] 
b = a[:2, 1:3]

# 配列のスライスは元の配列と同じデータを参照するため、
# スライスで作成した配列を変更すると元の配列も同様に変更される
# print(a[0, 1]) # "2"と表示
 
b[0, 0] = 77 # b[0, 0]はa[0, 1]と同じデータを参照 
# print(a[0, 1]) # "77"と表示

import numpy as np
 
# 以下の、階数2、形状(3, 4)の配列を作成
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
 
# 配列の真ん中の行にあるデータを取り出す方法は二通り用意されている
# 整数とスライスを同時に使う場合は階数が下がる
# スライスのみの場合は階数が変わらない
row_r1 = a[1, :] # aの2行目が階数1として取り出される
row_r2 = a[1:2, :] # aの2行目が階数2のまま取り出される
# print(row_r1, row_r1.shape) # "[5 6 7 8] (4,)"と表示
# print(row_r2, row_r2.shape) # "[[5 6 7 8]] (1, 4)"と表示
 
# 配列の列を取り出すときも同様の区別がなされる。
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
# print(col_r1, col_r1.shape) # "[ 2 6 10] (3,)"と表示
# print(col_r2, col_r2.shape) # "[[ 2]
                              # [ 6]
                              # [10]] (3, 1)"と表示


import numpy as np
 
a = np.array([[1,2], [3, 4], [5, 6]])

# ファンシーインデックス参照の例
# 表示される配列は形状(3,)を持ち、
# print(a[[0, 1, 2], [0, 1, 0]]) # "[1 4 5]"と表示
 
# 上記の例は以下と同様
# print(np.array([a[0, 0], a[1, 1], a[2, 0]])) #"[1 4 5]"と表示
 
# ファンシーインデックス参照では同じ要素の抽出も可能
# print(a[[0, 0], [1, 1]]) # "[2 2]"と表示
 
# 上記の例は以下と同様
# print(np.array([a[0, 1], a[0, 1]])) # "[2 2]"と表示

import numpy as np
 
# 要素抽出用に新しい配列を作成
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# print(a) # "[[ 1, 2, 3]
           # [ 4, 5, 6]
           # [ 7, 8, 9]
           # [10, 11, 12]]"と表示
 
# インデックスの配列を作成
b = np.array([0, 2, 0, 1])
 
# aからインデックス配列bを使って各行の要素を一つずつ取り出す
# print(a[np.arange(4), b]) # Prints "[ 1 6 7 11]"
 
# aからインデックス配列bを使って各行の要素を一つずつ変更する
a[np.arange(4), b] += 10
# print(a) # "[[11, 2, 3]
           # [ 4, 5, 16]
           # [17, 8, 9]
           # [10, 21, 12]]"と表示

import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2) # aから2より大きい値を持つ要素を見つける
# bool_idxの判定結果に即したブール型の要素を持った、
# aと同じ大きさの配列を返す 
# print(bool_idx) # "[[False False]
                  # [ True True]
                  # [ True True]]"と表示
 
# ブールインデックス配列は以下のようにして、
# bool_idxの判定結果Trueの要素のみを取り出し、
# 階数1の配列として表示する
# print(a[bool_idx]) # "[3 4 5 6]"と表示
 
# 上記のことは以下のように一行でも表せる
# print(a[a > 2]) # "[3 4 5 6]"と表示


import numpy as np
 
x = np.array([1, 2]) # 自動的にデータ型を選択
# print(x.dtype) # "int64"と表示
 
x = np.array([1.0, 2.0]) # 自動的にデータ型を選択
# print(x.dtype) # "float64"と表示
 
x = np.array([1, 2], dtype=np.int64) # 特定のデータ型を指定
# print(x.dtype) # "int64"と表示

import numpy as np
 
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
 
# 要素ごとの和; 共に配列を生成
# [[ 6. 8.]
 # [10. 12.]]
# print(x + y)
# print(np.add(x, y))
 
# 要素ごとの差; 共に配列を生成
# [[-4. -4.]
 # [-4. -4.]]
# print(x - y)
# print(np.subtract(x, y))
 
# 要素ごとの積; 共に配列を生成
# [[ 5. 12.]
 # [21. 32.]]
# print(x * y)
# print(np.multiply(x, y))
 
# 要素ごとの商; 共に配列を生成
# [[ 0.2 0.33333333]
 # [ 0.42857143 0.5 ]]
# print(x / y)
# print(np.divide(x, y))
 
# 要素ごとの平方根; 配列を生成
# [[ 1. 1.41421356]
 # [ 1.73205081 2. ]]
# print(np.sqrt(x))

import numpy as np
 
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])
 
# ベクトルの内積; 共に219
# print(v.dot(w))
# print(np.dot(v, w))
 
# 行列とベクトルの積; 共に階数1の配列[29 67]を生成
# print(x.dot(v))
# print(np.dot(x, v))
 
# 行列と行列の積; 共に階数2の配列
# [[19 22]
 # [43 50]]を生成
# print(x.dot(y))
# print(np.dot(x, y))

import numpy as np
 
x = np.array([[1,2],[3,4]])
# print(np.sum(x)) # すべての要素の和を計算; "10"と表示
# print(np.sum(x, axis=0)) # 列ごとの和を計算; "[4 6]"と表示
# print(np.sum(x, axis=1)) # 行ごとの和を計算; "[3 7]"と表示

import numpy as np
 
x = np.array([[1,2], [3,4]])
# print(x) # "[[1 2]
           # [3 4]]"と表示
# print(x.T) # "[[1 3]
             # [2 4]]"と表示
 
# 階数1の配列で転置行列を作ろうとしても何も起こらない
v = np.array([1,2,3]) 
# print(v) # "[1 2 3]"と表示
# print(v.T) # "[1 2 3]"と表示

import numpy as np
 
# 行列xの各行にベクトルvを加え、結果を行列yに入れる
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) # xと形状が等しい空の行列を作成
 
# ベクトルvを、ループを使って行列xの各行に加える
for i in range(4):
    y[i, :] = x[i, :] + v 
    # yは以下の通り
    # [[ 2 2 4]
    #  [ 5 5 7]
    #  [ 8 8 10]
    #  [11 11 13]]
 
# print(y)


import numpy as np
 
# 行列xの各行にベクトルvを加え、結果を行列yに入れる
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1)) # vを複製し4回重ねる
 
# print(vv) # "[[1 0 1]
          #   [1 0 1]
          #   [1 0 1]
          #   [1 0 1]]"と表示
 
y = x + vv # xとvvを要素ごとに加える
# print(y) # "[[ 2 2 4]
           # [ 5 5 7]
           # [ 8 8 10]
           # [11 11 13]]"と表示

import numpy as np
 
# 行列xの各行にベクトルvを加え、結果を行列yに入れる
 
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v # ブロードキャストを使用してvをxの各行に加える
# print(y) # "[[ 2 2 4]
         #  [ 5 5 7]
         #  [ 8 8 10]
         #  [11 11 13]]"と表示

import numpy as np
 
# ベクトルの外積を計算
v = np.array([1,2,3]) # vの形状は(3,)
w = np.array([4,5]) # wの形状は(2,)
 
# 外積を計算するには、まずvを形状(3, 1)の列ベクトルにし、
# wに対してブロードキャストして形状(3, 2)とする
# vとwの外積は以下の通り
# [[ 4 5]
#  [ 8 10]
#  [12 15]]
# print(np.reshape(v, (3, 1)) * w)
 
# 行列の各行にベクトルを加える
x = np.array([[1,2,3], [4,5,6]])
 
# xは形状(2, 3)を、vは形状(3,)を持つので、
# ブロードキャストして(2, 3)となる
# 求める行列は以下の通り
# [[2 4 6]
#  [5 7 9]]
# print(x + v)
 
# 行列の各列にベクトルを加える
# xは形状(2, 3)を持ち、wは形状(2,)を持つ
# xを転置すると形状(3, 2)となり、wに対してブロードキャストすると形状(3, 2)となる
# この結果を転置すると形状(2,3)となり、これが行列xの各列にベクトルwを加えたものとなる
# 結果は以下の通り
# [[ 5 6 7]
#  [ 9 10 11]]
# print((x.T + w).T)
 
# もしくは、wを形状(2, 1)の列ベクトルに変換すれば、
# xに対して直接ブロードキャストすることができる
# print(x + np.reshape(w, (2, 1)))
 
# 行列を定数倍する
# xは形状(2, 3)で、Numpyはスカラを形状()として扱う
# これらはブロードキャストして形状(2, 3)となり、以下の行列を生成
# [[ 2 4 6]
#  [ 8 10 12]]
# print(x * 2)

from imageio.v2 import imread, imwrite
import numpy as np
from PIL import Image

# JPEG画像を読み込みNumpyの配列に入れる 
# img = imread('assets/cat.jpg')
# print(img.dtype, img.shape) # "uint8 (400, 248, 3)"と表示
 
# 異なったスカラー数でカラーチャネルを調整することで
# 画像の色合いを変えられる。画像は形状(400, 248, 3)を持つ
# 形状(3,)の配列[1, 0.95, 0.9]をこれに掛ける
# ブロードキャストすることで、赤のチャネルは変化なく残り、
# 緑と青のチャネルはそれぞれ0.95と0.9が掛けられる
# g_tinted = img * [1, 0.95, 0.9]

# 色合いを変えた画像を300×300ピクセルにリサイズする 
# img_tinted = np.array(Image.fromarray(g_tinted.astype(np.uint8)).resize((300, 300)))

# 色合いを変えた画像をディスクに書き込む 
# imwrite('assets/cat_tinted.jpg', img_tinted)

import numpy as np
from scipy.spatial.distance import pdist, squareform
 
# 2次元空間に各行が点の配列を作成
# [[0 1]
#  [1 0]
#  [2 0]]
x = np.array([[0, 1], [1, 0], [2, 0]])
# print(x)
 
# xのすべての行の間のユークリッド距離を計算
# d[i, j]はx[i, :]とx[j, :]間のユークリッド距離で、
# dは以下の配列となる
# [[ 0. 1.41421356 2.23606798]
#  [ 1.41421356 0. 1. ]
#  [ 2.23606798 1. 0. ]] 
d = squareform(pdist(x, 'euclidean'))
# print(d)

import numpy as np
import matplotlib.pyplot as plt
 
# 正弦波の点に対応するxとyを計算
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
 
# matplotlibを用いてプロットを表示
# plt.plot(x, y)
# plt.show() # 画像を表示するにはshow()を呼び出す必要あり

import numpy as np
import matplotlib.pyplot as plt
 
# 正弦波・余弦波の点に対応するxとyを計算
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
 
# matplotlibを用いプロットを表示 
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
 
# 正弦波・余弦波の点に対応するxとyを計算
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
 
# 高さ2、幅1のサブプロットを設定し、最初のサブプロットを指定
plt.subplot(2, 1, 1)
 
# 最初のプロットを作成
# plt.plot(x, y_sin)
# plt.title('Sine')
 
# 二番目のサブプロットを指定し、二番目のプロットを作成 
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title('Cosine')

# 図を表示
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from imageio.v2 import imread

img = imread('assets/cat.jpg')
img_tinted = img * [1, 0.95, 0.9]
 
# 元の画像を表示
# plt.subplot(1, 2, 1)
# plt.imshow(img)
 
# 色合いを変えた画像を表示 
# plt.subplot(1, 2, 2)
 
# uint8以外のデータ型でimshowを使うと、変な結果になることがある
# これを防ぐため、表示する前に画像を明示的にuint8にする
# plt.imshow(np.uint8(img_tinted))
# plt.show()