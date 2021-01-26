import numpy as np
import mnist as mnist
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense, Dropout
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.utils.np_utils import to_categorical


def run():
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

    trainImgs = trainImgs.reshape((-1, 784))
    testImgs = testImgs.reshape((-1, 784))
    print(trainImgs.shape)
    print(testImgs.shape)

    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.1))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation='softmax'))

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy'],
    )

    model.fit(
        trainImgs,  # training data
        to_categorical(trainLabels),  # training targets
        epochs=3,
        batch_size=32,
        validation_data=(testImgs, to_categorical(testLabels))
    )

    # evaluate test data
    model.evaluate(testImgs, to_categorical(testLabels))

    # save model
    model.save_weights('mnist_weight.h5')


if __name__ == '__main__':
    run()
