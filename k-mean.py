import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
import seaborn as sb


def genDataThenPlot(nSample, nCentroid, debug) -> any:
    ps, centers = make_blobs(n_samples=nSample, centers=nCentroid, cluster_std=0.6, random_state=0)

    if debug == True:
        print(points[:, 0])
        print(points[:, 1])

    # sb.set_style("ticks")
    # sb.scatterplot(x=points[:, 0], y=points[:, 1])
    # plt.show()

    return ps


def runKmeanElbow(nTime, data) -> None:
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()


def runKmean(data, isPrintChart) -> None:
    km = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
    predict = km.fit_predict(data)
    print(predict)
    if isPrintChart:
        sb.set_style("ticks")
        sb.scatterplot(x=data[:, 0], y=data[:, 1])
        centroids = km.cluster_centers_
        sb.scatterplot(centroids[:, 0], centroids[:, 1], palette='husl')
        plt.show()


if __name__ == '__main__':
    print('k mean')
    sb.set()
    points = genDataThenPlot(100, 4, False)
    # print(points)
    # runKmeanElbow(10, points)
    runKmean(data=points, isPrintChart=True)
