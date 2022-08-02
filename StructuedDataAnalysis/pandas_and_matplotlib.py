from os import access
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## データ読み込み
df = pd.read_csv("./train_housing.csv", index_col=0)

## 最初の五行を表示
# print(df.head(n=5))

## データの次元数（行数，列数）
# print(df.shape)

## すべての列の名前を表示
# print(df.columns)

## 列ごとの基本情報を表示
# print(df.info())

## 数値データのみが入ったデータフレームの作成
df_num = df.select_dtypes(include=['number']) 
# print(df_num.info())

## 上で作成したデータフレームでSalesPriceと相関の高い上位10列を表示
df_corr = df_num.corr(method='pearson')['SalePrice']
# print(df_corr.nlargest(n=10)) # or
# print(df_corr.sort_values(ascending=False).head(10))
# print(df_corr.nsmallest(n=10)) # or
# print(df_corr.sort_values(ascending=True).head(10))

## SalesPrice列の分布の情報を表示 
df_sp = df_num['SalePrice']
# print(df_sp.describe())

## Pandasの組み込み関数を使ってSalesPrice列のヒストグラムを表示
# df.SalePrice.hist(grid=False, bins=30)
# plt.ylabel('Frequency')
# plt.show()

## OverallQualの固有値を表示
# print(df_num['OverallQual'].unique())

## OverallQual列からピボットテーブルを作成し、SalesPriceとの関係を表示
df_pt = df.pivot_table(index='OverallQual', values='SalePrice')
df_pt['SalePrice'] = df_pt['SalePrice'].astype('int64')
# print(df_pt)

## 上のデータフレームを棒グラフとして表示
# df_pt.plot.bar()
# plt.show()

## YearBuilt列の範囲を表示
df_yb = df_num['YearBuilt']
# print("The range of years build is from {:4d} to {:4d}.".format(df_yb.min(), df_yb.max()))

## YearBuiltを10年ごとにビン分割したYearBins列を生成
bins = list(range(1870, 2020, 10))
df_yb_bins = pd.cut(df_yb, bins)   
# print(df_yb_bins)

## SalesPriceとYearBins、OverallQualとの関係を箱ひげ図で表示
# df_num.boxplot(
#     column='SalePrice',
#     by='OverallQual',
#     grid=False
#     )

df_num['YearBuilt'] = df_yb_bins    
# df_num.boxplot(
#     column='SalePrice',
#     by='YearBuilt',
#     grid=False
#     )
# plt.show()

## SalesPriceとGrLivArea, GarageCars, GarageArea, TotalBsmtSFの関係を分布図として表示
# df_num.plot.scatter(x='GrLivArea', y='SalePrice')
# df_num.plot.scatter(x='GarageCars', y='SalePrice')
# df_num.plot.scatter(x='GarageArea', y='SalePrice')
# df_num.plot.scatter(x='TotalBsmtSF', y='SalePrice')
# plt.show()
