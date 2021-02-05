import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
import seaborn as sb
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

if __name__ == '__main__':
    print('titanic')
    train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    train = pd.read_csv(train_url)
    test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
    test = pd.read_csv(test_url)

    # # print(train.head())
    # print(train.describe())
    # print(train.columns.values)
    #
    # # check empty value
    # print(train.isna().head())
    # print(test.isna().head())
    #
    # # sum empty value
    # print(train.isna().sum())
    # print(test.isna().sum())
    #
    # # fill NA value
    train.fillna(train.mean(), inplace=True)
    test.fillna(test.mean(), inplace=True)
    print(train.isna().sum())
    print(test.isna().sum())
    #
    # print(train['Ticket'].head())
    # print(train['Cabin'].head())

    # group with survival count
    pclass = train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived',
                                                                                                  ascending=False)
    print(pclass)

    sex = train[['Sex', 'Survived']].groupby(by=['Sex'], as_index=False).mean().sort_values(by='Survived',
                                                                                            ascending=False)
    print(sex)

    sib = train[['SibSp', 'Survived']].groupby(by=['SibSp']).mean()
    print(sib)

    print(train.info())

    # drop
    train = train.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'PassengerId', 'SibSp', 'Parch', 'Fare'], axis=1)
    test = test.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'PassengerId', 'SibSp', 'Parch', 'Fare'], axis=1)

    labelEncoder = LabelEncoder()
    labelEncoder.fit(train['Sex'])
    labelEncoder.fit(test['Sex'])
    train['Sex'] = labelEncoder.transform(train['Sex'])
    test['Sex'] = labelEncoder.transform(test['Sex'])

    print('info 2')
    print(train.info())

    print('info 3')
    print(train.isna().sum())

    X = np.array(train.drop(['Survived'], axis=1).astype(float))
    y = np.array(train['Survived'])
    print(X)

    print('k mean')
    km = KMeans(n_clusters=2, max_iter=10000, algorithm='auto', init='k-means++')

    scaler = MinMaxScaler()
    scaled_X = scaler.fit_transform(X)

    predict = km.fit_predict(scaled_X)

    print('done')
    print(predict)
    print(y)

    print('summary')
    count = 0
    for i in range(len(predict)):
        # print("predict: %d : %d" % (predict[i], y[i]))
        if predict[i] == y[i]:
            count = count + 1

    print(count / len(predict))
