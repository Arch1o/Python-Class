"""
numpy 基础操作
"""
import numpy as np

"""
numpy添加元素
np.append（）
"""

arr01 = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(arr01)
print(arr01.shape)
# 添加元素，维度要保持一致
# 在0轴添加元素
print(np.append(arr01, [[7, 8, 9]], 0))
# 在1轴添加元素
print(np.append(arr01, [[7], [8]], 1))

"""
insert()
"""

print('-------------------------')
# 插入到0轴索引为1的位置处
arr02 = np.insert(arr01, 1, [[7, 8, 9], [10, 11, 12]], 0)
print(arr02)
# 插入到1轴索引为4的位置
arr03 = np.insert(arr01, 3, [7, 8], 1)
print(arr03)

"""
删除元素
    np.delete
"""

# 通过对应轴的索引删除
print('////')
arr04 = np.delete(arr01, 1, 1)
print(arr04)
# 通过拉平后的位置删除
arr05 = np.delete(arr01, [0, 4])
print(arr05)

"""
unique
    去重操作
"""

print('-------------------------')

arr06 = np.array([1, 3, 2, 3, 5, 2, 1])
arr07 = np.unique(arr06,
                  True,
                  True,
                  True)
print(arr07)
# (array([1, 2, 3, 5]),   ==> 去重后的数据
# array([0, 2, 1, 4],  dtype=int64),    ==> 去重后元素对应的索引
# array([0, 2, 1, 2, 3, 1, 0], dtype=int64),    ==> 原数据在被去重数据中所对应的索引
# array([2, 2, 2, 1], dtype=int64))   ==> 每个数据在原数据中出现的次数

"""
拉直操作
    ravel()：返回的是原始数组的视图（view），不产生副本，
    这意味着原始数据结构和内存位置保持不变。如果对返回的视图进行修改，
    原始数组也会相应地被修改。
    
    flatten()：总是返回原数据的副本，即使结果是一个一维数组，
    它与原始数据在内存中的位置不同。因此，对返回的数组进行修改不会影响原始数组。
    
    reshape()：可以用来将多维数组转换为指定的新形状，包括一维数组。
    当使用参数-1时，它可以像ravel()和flatten()一样将多维数组拉平为一维数组。
    但是，reshape(-1)特别之处在于，它可以自动计算缺失的维度大小，使得数组变形更加灵活。
"""

print('-------------------------')
# -1表示自动计算该维度的大小，以使得数组元素个数不变
arr07 = arr01.reshape(-1)
print(arr07)
print(arr07.shape)

arr08 = np.array([[[1, 2, 3],
                   [4, 5, 6]],
                  [[5, 6, 7],
                   [7, 8, 9]]])
print(arr08.shape)
# flat属性返回一个迭代器，可以用于遍历多维数组的所有元素。
arr09 = arr08.flat
print(arr09)
for i in arr09:
    print(i)

arr10 = arr08.flatten()
print(arr10)

arr10 = arr08.ravel()
print(arr10)


"""
转置
"""

print(arr01)
print('-------------------------')
arr11 = np.transpose(arr01)
print(arr11)
# 写法二
arr11 = arr01.T
print(arr11)
