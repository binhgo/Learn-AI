import numpy as np


def testNp1():
    arr = np.arange(15).reshape(3, 5)
    if arr is not None:
        print(arr)

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

    arr4 = np.arange(24).reshape(2, 3, 4)
    print(arr4)

    arr5 = np.array([1, 2, 3, 4])
    arr6 = np.array([5, 6, 7, 8])

    arr7 = arr5 - arr6
    print(arr7)

    arr7 = np.arange(100).reshape(4, 25)
    print(arr7)

    for row in arr7:
        print(row)


if __name__ == '__main__':
    testNp1()
