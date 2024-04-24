## 推导式 & 迭代问题
# 列表推导式
list1 = [v for v in range(5)]
print(list1)

# list1等价于下面list2
list2 = []
for v in range(5):
    list2.append(v)
print(list2)

list3 = [x+y for x in [1, 2] for y in (4, 5, 6)]
print(list3)
list4 = []
for x in [1, 2]:
    for y in (4, 5, 6):
        list4.append(x+y) #在列表的最后添加x+y
print(list4)

if 0:
    print('a') # 0 是一个布尔值。在大多数编程语言中，0 被视为假（false）
if 2:
    print('b') # 任何非零数值都被视为布尔值True

# 列表推导式的嵌套
    matrix = [[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]]
    
result1 = [[row[i] for row in matrix] for i in range(4)]  # 转置
print(result1)
# result1 等价与 result2
result2 = []
for i in range(4):
    temp=[row[i] for row in matrix] # 嵌套
    result2.append(temp)
print(result2)

temp1=[row[i] for row in matrix]
print(temp1)
# temp1 等价于 temp2

temp2 = []
for row in matrix:
    print(row)
    temp2.append(row[i])
print(temp2)

# 字典推导式
dic1 = {k: k+1 for k in range(1, 4)}  # {1: 2, 2: 3, 3: 4}
print(dic1)

# 遍历过程中可能出现的问题
list1 = ['a', 'b', 'c', 'd']
for i in list1:
    list1.remove(i)
print(list1)  # ['b', 'd'] 原因：遍历的过程，移除了原数据，索引改变
# 解决方法：浅拷贝/深拷贝
list1 = ['a', 'b', 'c','d']
list2 = list1.copy()  # 浅拷贝
for i in list2:
    list1.remove(i)
    print(list1)
# 深拷贝
# list2 = copy.deepcopy()



