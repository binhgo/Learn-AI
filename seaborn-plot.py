import seaborn as sb
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    print(x)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


def plot():
    print(sb.get_dataset_names())

    df = sb.load_dataset('tips')
    print(df.head(10))


def color():
    cl = sb.color_palette()
    sb.palplot(cl)
    plt.show()


def displot():
    iris = sb.load_dataset('iris')
    print(iris)
    sb.distplot(iris['petal_length'], kde=False)
    plt.show()


def joinplot():
    iris = sb.load_dataset('iris')
    sb.jointplot(x='petal_length', y='petal_width', data=iris)
    plt.show()


def pairplot():
    iris = sb.load_dataset('iris')
    sb.set_style("ticks")
    sb.pairplot(iris, hue='species', diag_kind='kde', kind='scatter', palette='husl')
    plt.show()


def stripplot():
    irisDf = sb.load_dataset('iris')
    sb.stripplot(data=irisDf, x='species', y='petal_length', jitter=True)
    plt.show()


if __name__ == '__main__':
    sb.set()
    stripplot()
    # pairplot()
    # joinplot()
    # displot()
    # color()
    # sinplot()
    # plt.show()
    # plot()
