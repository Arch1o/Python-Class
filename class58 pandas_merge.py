"""
merge（）
    left/right：两个合并的DataFrame对象
    how：需要执行合并的类型left，right，outer并集，inner交集
    on：指定列名用于连接，必须两个表都有，作为交集
    left_on，right_on：两个表的列名不一样，但含义一样
"""
import pandas as pd

left = pd.DataFrame({"id": [1, 2, 3, 4],
                     "name": ["张三", "李四", "王五", "赵六"],
                     "sub_id": ["sub1", "sub2", "sub3", "sub4"]})

right = pd.DataFrame({"id": [1, 2, 3, 4],
                      "name": ["张三1", "李四1", "王五1", "赵六1"],
                      "sub_id": ["sub11", "sub22", "sub3", "sub44"]})

print(left)
print(right)
"""
how：
    inner：默认的模式，使用指定key值的交集
    outer：使用指定key值做并集
"""
print("===============指定单个key值=sub_id===================")
# 指定单个key值
result01 = pd.merge(left, right, on="sub_id", how="outer")
print(result01)

print("=================指定多个key值==================")

# 指定多个key值
result02 = pd.merge(left, right, on=["id", "sub_id"], how="inner")
print(result02)

print("=================不指定key值 ==================")
# 不指定key值 ==> 没有指定的时候，默认将相同的key值作为指定连接键
result03 = pd.merge(left, right, how="inner")
print(result03)  # Empty DataFrame
