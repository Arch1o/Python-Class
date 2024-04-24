"""
open
打开文件的方式
open（打开文件的路径）
"""
import warnings
import wsgiref.validate

file = open("./test.txt", "r", encoding="utf-8")  # “r” 为只读
print(file)

# 读取内容
# result = file.read()
# print(result)

# 读取一行数据
result01 = file.readline()
print(result01)
print("--------------------")
print(next(file))  # 可遍历的迭代器对象

# result01 = file.readline()
# print(result01)
# result = file.readlines()
# print(result)  # ['111\n', '222\n', '3333'] 存在换行符
print("---------for line in file:-----------")
for line in file:
    print(line)

"""
关闭文件
"""
file.close()

"""
使用 with open 的方式打开文件
"""
print("--------------------")
# 退出代码块文件自动关掉
with open("./test.txt", "r", encoding="utf-8") as file:
    print(file)
    result = file.readlines()
    print(result)

# 编辑
with open("./test01.txt", "w", encoding="utf-8") as w:
    w.write("这是我写入的第一行\n")
    w.write("这是我写入的第二行\n")
    # 每次写入的数据会覆盖

# 想在原来的基础上继续添加
with open("./test01.txt", "a", encoding="utf-8") as w:
    w.write("这是我写入的第三行\n")
    w.write("这是我写入的第四行\n")

"""
使用tell查看文件的指针位置
使用seek设置指针位置：offset参数表示要移动的偏移量，而whence参数表示偏移量的起始位置。
默认情况下，whence的值为0，表示从文件开头开始计算偏移量。
1是当前位置
2是结尾
"""
print("---------使用tell查看文件的指针位置-----------")
# w+ 覆盖读写模式
with open("test02.txt", "w+") as w:
    w.write("123\n")
    w.write("456\n")
    position = w.tell()  # 查看指针位置
    print(position)
    w.seek(0, 0)  # 设置指针位置
    print(w.tell())
    w.write("789\n")
    print("--------------------")
    result = w.readlines()
    print(result)


