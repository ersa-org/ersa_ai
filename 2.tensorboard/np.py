import numpy as np


def demo():
    # ndarray 对象
    d1arr = np.array([1, 2, 3, 4])
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    # 所有元素求和
    arr.sum()
    #  矩阵垂直方向求和
    arr.sum(axis=0)
    #  水平方向求和
    arr.sum(axis=1)

    arr.min(axis=0)
    # arr.max()
    # 数组中是否有满足条件的元素
    np.any(arr > 4)
    ## 摊平
    flat = arr.flatten()
    print(flat)


    ## 转数组
    lst =arr.tolist()
    for i in lst:
        print(i)
    print(list)

    # 判断矩阵内是否有 0 或者 false 数据
    r = arr.all()
    print(r)

    # 深拷贝
    cpy = arr.copy()
    isDeep = cpy is arr
    print(isDeep)














if __name__ == "__main__":
    demo()
