"""
concat
    objs：
    axis：0沿着行索引的方向；1是沿着列索引的方向
    join：inner/outer ==> 默认值是outer 索引的交集或并集
    ignore_index ==> 重置索引
"""
import pandas as pd

a = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                  "B": ["B0", "B1", "B2", "B3"],
                  "C1": ["C0", "C1", "C2", "C3"],
                  "D2": ["D0", "D1", "D2", "D3"]}, index=[0, 1, 2, 3])

b = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"],
                  "B": ["B4", "B5", "B6", "B7"],
                  "C": ["C4", "C5", "C6", "C7"],
                  "D": ["D4", "D5", "D6", "D7"]}, index=[4, 5, 6, 7])
print(a)
print(b)
print('======================')
result01 = pd.concat([a, b], axis=0, keys=["a", "b"], join="inner")
print(result01)

print('======================')

# sample
'''
这段代码是使用Python中的pandas库来对DataFrame对象进行抽样操作。
具体来说，它从DataFrame对象a中按照指定的轴（axis=1）随机抽取2个样本。
'''
print(a.sample(n=2, axis=1))  # 列采样
print('-----------------------')
# 有放回的采样
print(a.sample(n=6, replace=True))

print('-----------------------')
# 无放回的采样 ==> 采样样本数需要小于对应的行列数
print(a.sample(n=4, replace=False))
