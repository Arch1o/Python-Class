"""
pandas
    数据处理分析
    pandas的数据结构：series dataframe
        serie：带标签的一维数组
"""
import numpy as np
import pandas as pd

arr01 = np.array([1, 2, 3, 4, 5])
print(arr01)  # [1 2 3 4 5]
print(type(arr01))  # <class 'numpy.ndarray'>
print(arr01.shape)

# 使用numpy格式创建Series
print('-----------------------')
series01 = pd.Series(arr01)
print(series01)
"""
标签 数据
0    1
1    2
2    3
3    4
4    5
"""
print(type(series01))  # <class 'pandas.core.series.Series'>
print(series01.shape)

# 自定义标签内容
print('-----------------------')
series01 = pd.Series(arr01, index=["a", "b", "c", "d", "e"])
print(series01)

# 直接使用列表创建Series
print('-----------------------')
series02 = pd.Series([1, 2, 3, 4, 5], index=[101, 102, 103, 104, 105])
print(series02)
print(type(series02))
print(series02.shape)

# 使用字典创建Series

print('-----------dict----------')
dict01 = {"a": 1, "b": 2, "c": 3}
series03 = pd.Series(dict01, index=["a", "b", "d"])  # 只能取到字典里有的索引
"""
a    1.0
b    2.0
d    NaN
"""
print(series03)
print(type(series03))
print(series03.shape)
print(series03["a"])

# 使用标量创建Series
print('-----------------------')
series04 = pd.Series(5, index=["a", "b", "c"])  # 将标量赋值给每个索引
print(series04)
print(series04.shape)

# 二维数组创建Series
print('-----------------------')
try:
    arr02 = np.array([[1, 2, 3],
                      [4, 5, 6]])
    series05 = pd.Series(arr02)
    print(series05)
except Exception as e:
    print(e)  # Data must be 1-dimensional, got ndarray of shape (2, 3) instead

# 换一种思路 将高维中的列表转化成一个元素
print('-----------------------')
series06 = pd.Series([[1, 2, 3], [4, 5, 6]])
print(series06)
print(series06.shape)

"""
访问Series数据
"""

print("============================")
print(series01)

# 使用位置索引访问
"""
这个警告是因为在将来的版本中，使用整数作为键来访问Series对象的行为将会改变。
为了保持一致性，建议使用iloc方法来通过位置访问值。你可以将代码修改为：
"""
print(series01[4])  # 5

print(series01.iloc[4])  # <class 'numpy.int32'>

print(type(series01[4]))  # <class 'numpy.int32'>

print(type(series01.iloc[4]))  # <class 'numpy.int32'>

print('-----------使用标签索引访问------------')
# 使用标签索引访问  相当于字典中使用键来访问
print(series01["a"])  # 1

print('------------切片访问-----------')
# 切片访问
print(series01[1:4])
print(type(series01[1:4]))  # <class 'pandas.core.series.Series'>

print('-----------使用标签访问呢多个数据------------')
# 使用标签访问呢多个数据
print(series01[["a", "b", "e"]])

print('------------使用多个索引访问-----------')
# 使用多个索引访问
print(series01[[1, 2, 3]])

"""
这个警告是因为在将来的版本中，使用整数作为键来访问Series对象的行为将会改变。
为了保持一致性，建议使用iloc方法来通过位置访问值。你可以将代码修改为：  
"""
print('-----------------------')
print(series01.iloc[[1, 2, 3]])

# 查看标签索引/值
print('-----------属性----------')
print(series01.axes)  # [Index(['a', 'b', 'c', 'd', 'e'], dtype='object')]
print(series01.index)  # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print(series01.values)  # [1 2 3 4 5]
print(type(series01.values))  # <class 'numpy.ndarray'>
print(series01.dtype)

# 常用的方法
print('----------方法-----------')
print(series01.head())  # 查看头几条数据，默认5条
print(series01.tail())  # 查看后几条数据，默认5

# 检测缺失值
print('-----------------------')
series07 = pd.Series([1, 2, 3, None, 4, 5])
print(series07.isnull())  # 是否为缺失
print(series07.notnull())  # 是否不是缺失

print('-----------------------')
series07 = pd.Series([1, 2, 3, "", 4, 5])  # 空字符串不会被识别为none值
print(series07)
print(series07.isnull())  # 是否为缺失
print(series07.notnull())  # 是否不是缺失

