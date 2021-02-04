import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
import seaborn as sb

if __name__ == '__main__':
    print('titanic')
    train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    train = pd.read_csv(train_url)
    test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
    test = pd.read_csv(test_url)

    # print(train.head())
    print(train.describe())
    print(train.columns.values)

    # check empty value
    print(train.isna().head())
    print(test.isna().head())

    # sum empty value
    print(train.isna().sum())
    print(test.isna().sum())

    # fill NA value
    train.fillna(train.mean(), inplace=True)
    test.fillna(test.mean(), inplace=True)
    print(train.isna().sum())
    print(test.isna().sum())

    print(train['Ticket'].head())
    print(train['Cabin'].head())
