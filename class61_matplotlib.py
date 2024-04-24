"""
matplotlib
"""
import numpy as np
from matplotlib import pyplot as plt
import random

"""
pycharm：弹窗
jupyter：
    %matplotlib inline  # 嵌入
    %matplotlib tk  # 弹窗
"""

x = np.arange(10)
print(x)
y = x * 5 + 2
y1 = x*3+5
print(y)

# 设置字体
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置中文字体==>微软雅黑
# 声明图对象
fig = plt.figure(figsize=(8, 5), num='num1')
# 设置参数
plt.plot(x, y, label="y")
plt.plot(x, y1, label="y1")
# 对坐标轴命名
plt.xlabel("x")
plt.ylabel("y")
# 加上标题
plt.title("线性函数：y=x*5+2")
# 添加图例
plt.legend()
# 显示
plt.show()

"""
在一个图里画两个图
    plt.subplot（）
"""

plt.figure(figsize=(5, 8), num="sub")
plt.subplot(211)  # 其中第一位表示行数，第二位表示列数，第三位表示子图的索引
plt.plot(x, y, "r-o", label="y")
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=5*x+2")
plt.legend()

plt.subplot(212)
plt.plot(x, y1, "b--*", label="y1")
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=3*x+5")
plt.legend()

plt.show()

"""
柱状图
    plt.bar（）
"""

x = ["语文", "数学", "英语", "物理"]
print(np.arange(len(x)))
y = [80, 90, 95, 100]
y1 = [85, 98, 89, 80]
plt.figure(num="bar")
plt.bar(x, y, width=0.25, label="student1", align="edge")
plt.bar(np.arange(len(x))-0.125, y1,  width=0.25, align="center", label="student2")
plt.xlabel('科目')
plt.ylabel('成绩')
plt.legend()

# 图上添加文本
for a, y_score, y1_score in zip(np.arange(len(x)), y, y1):
    plt.text(a+0.0625, y_score+0.5, y_score)
    plt.text(a-0.1825, y1_score+0.5, y1_score)
plt.show()

"""
饼状图
"""
plt.figure(num="pie")
# autopct是一个格式字符串，用于显示每个饼图部分的百分比
plt.pie(y, labels=x, autopct="%1.2f%%")  # autopct参数设置为空字符串，表示不显示每个饼图部分的百分比。
plt.legend()
plt.show()


"""
直方图
    概率分布，显示一组数值序列在给定范围内出现的概率
    需要将整个数值范围划分成多个区间
    hist() 是 plt 模块中的一个函数，用于绘制直方图。
    bins 参数指定了直方图的分组区间，这里设置为 [0, 0.2, 0.4, 0.6, 0.8, 1.0]，表示将数据分为五个区间进行统计。
"""
a = np.random.random(100)
# print(a)
plt.hist(a, bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0], density=True)
plt.show()

"""
散点图
"""
a = np.random.randint(0, 20, 50)
b = np.random.randint(0, 20, 50)
print(a)
print(b)
plt.figure(num="scatter")
plt.scatter(a, b, color="r", label="ab")
plt.legend()
plt.show()
