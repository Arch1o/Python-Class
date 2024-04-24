import numpy as np
import pandas as pd

"""
DataFrame: 表格型的数据结构，既有行标签（index），也有列标签（columns）
    是一种表格型的数据结构，取出一列或一行数据相当于一个Series
"""

df01 = pd.DataFrame([1, 2, 3, 4, 5])
print(df01)
print(type(df01))  # <class 'pandas.core.frame.DataFrame'>
print(df01.shape)  # (5, 1) 二维的表格数据

df01 = pd.DataFrame([1, 2, 3, 4, 5],
                    index=[101, 102, 103, 104, 105],
                    columns=["第一列"])
print(df01)

# 创建多列的数据类型
print('--------------------------')
arr01 = np.arange(12).reshape(4, 3)
print(arr01)

print('--------------------------')
# 通过多维数据来创建dataframe对象
df02 = pd.DataFrame(arr01,
                    index=[101, 102, 103, 104],
                    columns=[1, 2, 3])

print(df02)
print(df02.shape)

# 通过嵌套列表创建df对象
print('--------------------------')
data = [["zhangsan", 15], ["lisi", 14], ["wangwu", 15]]
df03 = pd.DataFrame(data, index=["a", "b", "c"], columns=[1, 2])
print(df03)
print(df03.shape)
print(df03.dtypes)  # 查看每一列的数据类型

# 通过字典嵌套列表创建df
print('--------------------------')  # 键值对应列的名称
data = {"name": ["zhangsan", "lisi", "wangwu"],
        "age:": [13, 14, 15],
        "num": ["001", "002", "003"]}
df04 = pd.DataFrame(data)
print(df04)

# 通过列表嵌套字典创建df ==> 比较常见
print('--------------------------')  # 键值对应列的名称
data = [{"name": "zhangsan", "age": 15, "num": "001"},
        {"name": "lisi", "age": 14, "num": "002"},
        {"name1": "wangwu", "age": 15, "num": "003"}]
df05 = pd.DataFrame(data, index=[1, 2, 3])
print(df05)

#  使用字典嵌套Series创建df
print('--------------------------')
data = {"name": pd.Series(["zhangsan", "lisi", "wangwu"], index=[1, 2, 3]),
        "age": pd.Series([15, 14, 15], index=[1, 2, 3]),
        "num": pd.Series(["001", "002", "003", "004"], index=[1, 2, 3, 4])}
df05 = pd.DataFrame(data)
print(df05)

"""
df常用属性
"""

print('--------------------------')
print(df02)
print(df02.ndim)  # 2
print(df02.size)  # 12
print(df02.dtypes)  # 每一列的数据类型
print('--------------------------')
print(df02.axes)  # 返回列表
print(df02.index)
print(df02.columns)
# 转置
print('--------------------------')
print(df02.T)
print(df02.values)
print(type(df02.values))  # <class 'numpy.ndarray'>

"""
df方法
"""

print('--------------------------')
print(df02.head(n=2))
print(df02.tail(n=2))
print(df02.info())
print('--------------------------')
print(df02.describe())  # 对数值型数据进行统计信息的描述
print('--------------------------')
print(df02.shift(periods=1, axis=0, fill_value="fill_value 必须是一个标量"))  # 移动行/列  --> 形状不变
# periods=1表示移动的行数为1，
# axis=0表示沿着行方向进行移动，
# fill_value=某个标量表示使用指定的标量作为填充值。

"""
     1   2   3                               1    2    3   
101  0   1   2                        101  NaN  NaN  NaN
102  3   4   5                        102  0.0  1.0  2.0
103  6   7   8                        103  3.0  4.0  5.0
104  9  10  11                        104  6.0  7.0  8.0
"""

"""
通过索引对df数据进行操作
    返回的是一个Series
    iloc -- 位置索引
"""

# lioc
print('=========================')
print(df02)
# 取一个元素
print(df02.iloc[1, 1])
print('------------取一行数据--------------')
# 取一行数据
print(df02.iloc[1, :])
print('--------------------------')
# 取一列数据
print(df02.iloc[:, 1])

"""
通过切片的方式对df数据进行操作
    返回的是一个df
    iloc -- 位置索引
"""

print('=========================')
# 取一个元素
print(df02.iloc[[1], [1]])
print(type(df02.iloc[[1], [1]]))  # <class 'pandas.core.frame.DataFrame'>
print('--------------------------')
# 取一行数据
print(df02.iloc[[1]])
print('--------------------------')
# 取一列数据
print(df02.iloc[:, [1]])
# 取出前两行的前两列
print('--------------------------')
print(df02.iloc[:2, :2])  # 0~1

print('=========================')
# 索引和切片
list01 = [1, 2, 3, 4, "5"]
print(list01[2])  # 索引
print(list01[:2])  # 0~1 切片[1, 2]

"""
按照列名表标签称取出数据
"""

print('=========================')
print(df05)
print('--------------------------')
print(df05["name"])

# 取出两列
print(df05[["name", "age"]])
print(type(df05[["name", "age"]]))  # <class 'pandas.core.frame.DataFrame'>

# 改变索引
df02.index = ["a", "b", "c", "d"]
print(df02)

"""
按照行名表标签称取出数据
    loc -- 标签索引
"""

print('--------------------------')
print(df02.loc['a'])
print(type(df02.loc['a']))  # <class 'pandas.core.series.Series'>
print(type(df02.loc[['a']]))  # <class 'pandas.core.frame.DataFrame'>  双括号格式df
print('--------------------------')

"""
作业：
    读取每一个班级的学生信息和分数文件
    最终全校所有学生信息和分数在一个df对象里
    columns：包含学号、年纪、班级、姓名、语文、数学、英语
"""
