## 函数02
# 迭代器： iter（），next（）
# iter
list01 = ["a", "b", 1, 2, 4]
it = iter(list01)
print(it)
print(type(it)) # <class 'list_iterator'>
print(next(it)) # 将迭代对象遍历一遍
print(next(it))
print(next(it))