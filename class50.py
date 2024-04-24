"""
数组的运算, 广播机制
"""
import numpy as np

# 数据的四则运算

arr01 = np.array([1, 2, 3])
arr02 = np.array([4, 5, 6])
arr03 = np.array([2])
arr04 = np.array([1, 1, 1, 1])

"""
四则运算
    加减乘除
    要求：shape 保持一致 或者符合广播机制
    每个元素都进行加减乘除
"""

print(arr01 + arr02)
# print(np.add(arr01, arr02))

print(arr01 - arr02)
# print(np.subtract(arr01, arr02))

print(arr01 * arr02)
# print(np.multiply(arr01, arr02))

print(arr01 / arr02)
# print(np.divide(arr01, arr02))

# 为什么 print(arr01 + arr04) 会报错 ，但下式不会
print(arr01 + arr03)  # [3 4 5]

"""
广播机制
    解决数组中不同shape之间的算数运算问题
    相加从最后一个维度开始，要求至少shape最后一个维度相同，其他维度可以通过广播机制自动进行扩充相加
"""

print("-------------------")
# 维度不相同
arr05 = np.array([[1, 2, 3]])
print(arr05.shape)  # (1, 3)
print(arr01 + arr05)  # [[2 4 6]]

print("-------------------")
arr06 = np.array([[[5, 6, 7]]])
arr07 = np.array([[[1, 2, 3]],
                  [[4, 5, 6]]])
print(arr06.shape)  # (1, 1, 3)
print(arr07.shape)  # (2, 1, 3)
arr08 = arr06 + arr07  # 可以相加
print(arr08.shape)


