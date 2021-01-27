import numpy as np
import pandas as pd

if __name__ == '__main__':
    s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
    print(s)

    d = pd.date_range('20200101', periods=6)
    print(d)

    r64 = np.random.randn(6, 4)
    arr = [1, 2, 3, 4, 5, 6]
    df = pd.DataFrame(r64, index=arr, columns=list('ABCD'))
    print(df)

    df.head(int=1)
