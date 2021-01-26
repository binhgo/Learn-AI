import numpy as np
import mnist as mnist
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense, Dropout
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.utils.np_utils import to_categorical


def reloadWeight():
    testImgs = mnist.test_images()
    testLabels = mnist.test_labels()
    print(testImgs.shape)
    print(testLabels.shape)

    testImgs = (testImgs / 255) - 0.5
    testImgs = testImgs.reshape((-1, 784))
    print(testImgs.shape)

    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.1))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation='softmax'))

    model.load_weights("mnist_weight.h5")

    predict = model.predict(testImgs[0:5])
    print(predict)
    max = np.argmax(predict, axis=1)
    print(max)


if __name__ == '__main__':
    reloadWeight()
