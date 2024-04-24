"""
apply 函数
    操作行/列的数据
"""
import pandas as pd
import numpy as np


data = {"name": pd.Series(["zhangsan", "lisi", "wangwu"], index=[1, 2, 3]),
        "age": pd.Series([15, 14, 15], index=[1, 2, 3]),
        "num": pd.Series(["001", "002", "003", "004"], index=[1, 2, 3, 4])}
df01 = pd.DataFrame(data)
print(df01)
print('-----------------------')


# 在数据前加上前缀
def func01(x):
    # print(x)  # x在这里是每行的数据
    # print(x["num"])  # 用标签索引对num进行前缀的添加
    # print(type(x))  # <class 'pandas.core.series.Series'>
    x["num"] = "class01_" + x["num"]
    # print('-----------------------')
    return x

"""
apply函数讲每一行/列的数据输入到func进行操作 返回一个完整df
"""
df02 = df01.apply(func=func01, axis=1)  # 二维数据：0是列 1是行
"""
它将一个名为df01的DataFrame的每一行应用一个名为func01的函数，然后将结果赋值给名为df02的新DataFrame
"""
print(df02)
print(type(df02))  # <class 'pandas.core.frame.DataFrame'>

# 使用匿名函数
print('-----------------------')
'''
这段代码是使用Pandas库中的apply()函数对DataFrame df01进行操作。
它的作用是将df01中的每一行应用一个lambda函数，该函数检查每一行的"age"列是否为NaN（非数字），如果不是NaN，则返回该值，否则返回0。
'''
series01 = df01.apply(func=lambda x: x["age"] if not np.isnan(x["age"]) else 0, axis=1)
print(series01)
print(type(series01))  # <class 'pandas.core.series.Series'>
"""
1    15.0
2    14.0
3    15.0
4     0.0
"""

"""
pipe
    对所有元素
"""
print('-----------------------')
df03 = pd.DataFrame(np.random.randn(4, 3), columns=["c1", "c2", "c3"])
print(df03)
print('-----------------------')
df04 = df03.pipe(func=lambda x: x+2)  # 每个元素加2
print(df04)
print(type(df04))  # <class 'pandas.core.frame.DataFrame'>


"""
map（）
"""
print('-----------------------')
series02 = df03["c1"].map(lambda x: abs(x))  # 绝对值
print(series02)
print(type(series02))  # <class 'pandas.core.series.Series'>
print('-----------------------')
df05 = df03.map(lambda x: abs(x))  # 对每个元素进行操作
print(df05)
print('-----------------------')
df06 = df03.apply(func=lambda x: abs(x), axis=0)
print(df06)

"""
百分比变化
"""
print('=========百分比变化============')
series03 = pd.Series([1, 2, 3, 4, 5, 4])
# 计算每个元素与前一个元素所增加的百分比
print(series03.pct_change())
print('-----------------------')

df07 = pd.DataFrame([[1.1, 2, 3],
                     [4, 5.3, 6],
                     [7, 8, 9.2]],
                    columns=["c1", "c2", "c3"])  # 默认对列进行操作
print(df07.pct_change(axis=1))  # 改成对行进行操作


"""
协方差
cov()
    衡量两个变量之间线性关系的统计量
"""
print('=========协方差===========')
series04 = pd.Series(np.random.randn(6))
print(series04)
print(series03.cov(series02))  # -0.6473308868848839 ==> 越接近1相关度越高
print(df07.cov())  # 斜对称矩阵
"""
          c1             c2        c3
c1  8.703333==>c1和c1求  8.845  9.146667
c2  8.845000==>c2和c1求  9.030  9.290000
c3  9.146667==>c3和c1求  9.290  9.613333
"""


"""
相关系数
"""
print('=========相关系数===========')
print(series03.corr(series02))
print(df07.corr())


"""
分组操作
"""
print('=========分组操作===========')
print(df01)
# 根据年龄进行分组
result = df01.groupby("age")
print(result)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001BA59003F50>
# 查看分组结果
print(result.groups)  # {14.0: [2], 15.0: [1, 3]} ==>标签 + 索引
# 查看分组后的数据
print(result.get_group(15))
print('-----------------------')
# 通过遍历result查看结果
for label, group_data in result:
    print(label)
    print(group_data)

