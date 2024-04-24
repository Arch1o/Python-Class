"""
numpy 介绍
    一个运行速度非常快的数学库，主要用于数组计算
    核心数据结构 ndarray（n维数组）
"""

import numpy as np
print(np.__version__)  # 1.26.4

# 创建一个数组
arr01 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
print(arr01)
print(type(arr01))  # <class 'numpy.ndarray'>
# 元素个数
print(arr01.size)
# 数组的形状
print(arr01.shape)  # (2, 4)
# 最外层列表的元素个数
print(len(arr01))  # 2
# 数组的维度 2维数组为矩阵
print(arr01.ndim)  # 2
# 数组的存储类型
print(arr01.dtype)  # int32
# 数据类型进行转换
arr01 = arr01.astype(np.int64)
print(arr01.dtype)  # int64

print('-------------------------')
list01 = [[1, 2, 3],
          [4, 5, 6]]
# 取出元素“3”
print(list01[0][2])  # 分层索引
print(arr01[0][2])  # arry也可以通过这种方式取出元素

print('-------------------------')
list02 = [[[1, 2, 3],
           [4, 5, 6]],
          [[7, 8, 9],
          [2, 3, 4]]]
arr02 = np.array(list02)
print(list02[1][1][2])
print(arr02[1][1][2])
# 对于数组来说，另一种方法也可以获取其中的元素，列表不适用
print(arr02[1, 1, 2])
# 用上述方法可以余子式
print(arr02[0, :, 1:])  # [[2 3]，[5 6]]
# 切片不降维，索引降低维度；如果保持维度不变，就不能用索引！！！
print(arr02[0, :, 1])  # [2 5]
print('-------------------------')
print(arr02.shape)
print(arr02.ndim)


