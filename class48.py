"""
reshape array 创建
"""
import numpy as np

"""
bool 索引
"""

list01 = [[[1, 2, 3],
           [4, 5, 6]],
          [[7, 8, 9],
           [2, 3, 4]]]
arr01 = np.array(list01)

print(arr01 > 5)
print(arr01[arr01 > 5])  # 布尔索引 取出元素 [6 7 8 9] 结果为1维

"""
修改数组的形状与维度
    reshape（）
    取出所有元素重新排列，要求size不变
"""

print(arr01.size)  # 12 元素个数
print(arr01.shape)  # (2, 2, 3) 形状
print(arr01.ndim)  # 3 维度

# 修改为4*3的数组
arr02 = arr01.reshape(4, 3)
print(arr02)
print(arr02.shape)  # (4, 3)
print(arr02.ndim)  # 2

arr02 = arr01.reshape(3, 4)
print(arr02)

print('-----------------------')
arr03 = arr02.reshape(2, 2, 3)
print(arr03)
arr03 = arr02.reshape(12)
print(arr03)

print('-----------------------')
# -1为占位符，自动计算所需元素多少
arr04 = arr02.reshape(-1)
print(arr04)
arr04 = arr02.reshape(2, -1, 3)
print(arr04)

"""
常用的创建数组方式
"""

print('-----------------------')
# 创建一个全是0的数组
arr05 = np.zeros((2, 2, 4), dtype=np.int64)
print(arr05)
print(arr05.dtype)

# 创建全是1的数组
arr06 = np.ones((2, 2, 4))
print(arr06)
print(arr06.dtype)

arr06 = np.ones_like(arr02)
print(arr06)

# 用其他的数组作为样板创建
arr07 = np.zeros_like(arr02)
print(arr07)

print('-----------------------空数组')
# 创建空数组，里面有数据占位
arr08 = np.empty((2, 2, 4))
print(arr08)

"""
创建区间数组
    np.range（起始值，终止值，步距） 
    # 左闭右开
"""

print('-----------------------')
arr09 = np.arange(1, 10, 1).reshape(3, 3)
print(arr09)

"""
等差数组
    np.linspace()
    endpoint：默认为True，表示生成的数列包含区间的结束点；如果设置为False，则不包含结束点。
    retstep：默认为False，表示不返回步长；如果设置为True，则返回步长。
"""

print('-----------------------')
arr10 = np.linspace(1, 10, 5, True, True)
# arr10 是一个包含5个元素的等差数列，范围从1到10，步长为(10-1)/(5-1)=1.4。
print(arr10)

"""
等比数组
    np.logspace()
    start：序列的起始值，以对数形式表示。
    stop：序列的结束值，以对数形式表示。
    num：要生成的样本数量，默认为50。
    endpoint：是否包含区间的结束点，默认为True。
    base：对数的底数，默认为10.0。
    dtype：输出数组的数据类型，默认为None，表示根据输入数据推断数据类型。
"""

print('-----------------------')
arr11 = np.logspace(0, 1, 6, True, 32)
print(arr11)
