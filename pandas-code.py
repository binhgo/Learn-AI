import numpy as np
import pandas as pd

if __name__ == '__main__':
    s = pd.Series([2, 2, 3, 4, 5, 6, 7, 8])
    print(s)

    d = pd.date_range('20200101', periods=6)
    print(d)

    r64 = np.random.randn(6, 4)
    arr = [1, 2, 3, 4, 5, 6]
    df = pd.DataFrame(r64, index=arr, columns=list('ABCE'))
    print(df)

    df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": 2.0,
            "C": "QWE",
            "D": np.array([3] * 4, dtype="int32"),
        }
    )
    print(df2)
    print(df2.index)
    print(df2.columns)
    print(df2.A)
    df2.at[1, "A"] = 15
    print(df2)

    df3 = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
    df3.to_csv("df3.csv")

    df4 = pd.read_csv("df3.csv")
    df4.columns = ["A", "B", "C", "D", "E", "F"]
    print(df4)
    # df.head(int=1)
