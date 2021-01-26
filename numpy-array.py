import numpy as np


def testNp1():
    arr = np.arange(15).reshape(3, 5)
    print(arr)
    print(arr.shape)
    print(arr.ndim)
    print(arr.size)

    arr2 = np.array([1, 2, 3, 4])
    print(arr2)
    print(type(arr2))

    arr3 = np.array([(1, 2, 3), (4, 5, 6)])
    print(arr3)
    arr3 += 1
    print(arr3)


if __name__ == '__main__':
    testNp1()
