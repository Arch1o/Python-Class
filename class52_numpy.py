"""
numpy
"""
import numpy as np

"""
区别元素相乘 与矩阵相乘的区别
"""

arr01 = np.arange(6).reshape((2, 3))
arr02 = np.arange(7, 13).reshape((2, 3))
print(arr01)
print(arr02)

# 元素相乘
print('-------------------------')
print(arr01*arr02)
print(np.multiply(arr01, arr02))

# 矩阵相乘 m=n
print('-------------------------')
arr03 = np.arange(6).reshape((2, 3))
arr04 = np.arange(7, 13).reshape((3, 2))
print(arr03)
print(arr04)
print('-------------------------')
print(np.matmul(arr03, arr04))
print(np.dot(arr03, arr04))

"""
python中常用的数学统计指标
"""

print('===========================')
arr05 = np.arange(1, 28).reshape(3, 3, 3)
print(arr05)
print(np.amin(arr05))  # 最小
print(np.amax(arr05))  # 最大
print(arr05.mean())  # 均值
# 按照行列层计算
print('-------------------------')
print(np.amin(arr05, 0))
print('-------------------------')
print(np.amin(arr05, 1))
print('-------------------------')
print(np.amin(arr05, 2))
print('-------------------------')
print(np.amax(arr05, 1))
print(np.ptp(arr05, 1))  # 最大值-最小值
print(np.median(arr05))  # 中位数
print(np.var(arr05))  # 方差
print(np.std(arr05))  # 标准差

"""
排序
"""

print('-------------------------')
arr06 = np.array([1, 3, 2, 5, 4, 6, 1])
print(sorted(arr06))  # 返回的结果是list
print(np.sort(arr06))  # 返回的结果np array

# 多维数组的排序
arr07 = np.array([[1, 3, 2, 4],
                  [9, 8, 0, 3]])
try:
    print(sorted(arr07))
except Exception as e:
    print(e)  # 报错 sorted可以给list排序
finally:
    print('-------------------------')
    list01 = list(arr07)  # [array([1, 3, 2, 4]), array([9, 8, 0, 3])]
    print(list01)  # 无法强转arr为list

# 那创建一个list试一下sorted
list02 = [[9, 3, 2, 4], [9, 8, 0, 3]]
print(sorted(list02))  # [[9, 3, 2, 4], [9, 8, 0, 3]]
# sorted给list排序 按照第一个元素大小排 第一个相等就排第二个

print('====================')
# 用np的sort试试
print(arr07)
print(np.sort(arr07))  # [[1 2 3 4], [0 3 8 9]]
print(np.sort(arr07, 0))
print(np.sort(arr07, 1))

"""
where索引
"""

print('====================')
print(arr07)
print(arr07[arr07 > 5])  # bool索引
print(np.where(arr07 > 5))
# (array([1, 1], dtype=int64), array([0, 1], dtype=int64
       #  ^  ^ 行索引                  ^  ^ ；列索引

"""
获取最大值最小值的索引位置
"""

print('====================')
print(arr07)
print(np.argmin(arr07))
print(np.argmax(arr07))
print(np.argmin(arr07, 1))


"""
保存
"""

print('====================')
# with open("arr07.txt", "wb") as w:
# wb二进制写入
#     w.write(arr07)

# 保存
np.save("arr07.npy", arr07, allow_pickle=True)
# 加载
result = np.load("arr07.npy")
print(result)

