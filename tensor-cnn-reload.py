import numpy as np
import mnist as mnist
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.utils.np_utils import to_categorical


def runCNN():
    trainImgs = mnist.train_images()
    trainLabels = mnist.train_labels()
    print(trainImgs.shape)
    print(trainLabels.shape)

    testImgs = mnist.test_images()
    testLabels = mnist.test_labels()
    print(testImgs.shape)
    print(testLabels.shape)

    trainImgs = (trainImgs / 255) - 0.5
    testImgs = (testImgs / 255) - 0.5

    trainImgs = np.expand_dims(trainImgs, axis=3)
    testImgs = np.expand_dims(testImgs, axis=3)
    print(trainImgs.shape)
    print(testImgs.shape)

    model = Sequential()
    model.add(Conv2D(8, 3, input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(10, activation='softmax'))

    model.load_weights("mnist_cnn.h5")

    predict = model.predict(testImgs[0:10])
    print(predict)

    max = np.argmax(predict, axis=1)
    print(max)


if __name__ == '__main__':
    runCNN()
