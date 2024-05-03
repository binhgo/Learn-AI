import concurrent.futures


def task01():
    print("task 01")


def task02():
    print("task 02")


if __name__ == '__main__':
    print("hello")
    threadPools = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    threadPools.submit(task01)
    threadPools.submit(task02)
    threadPools.shutdown(wait=False)

    print("main")
