"""
os 模块
"""
import os
import sys

# 避免转义符影响
dir_path = r"D:\PycharmProjects\pythonProject\PythonClass"
# 或者使用双斜杠或正斜杆

# 获取当前路径所在目录（父级）
print(os.getcwd())
# dirname()获取指定文件（夹）的父级
print(os.path.dirname(__file__))
# 获取当前文件的绝对路径
print(os.path.abspath(__file__))

"""
找到其他文件绝对路径的方法
join 拼接路径
这种方法可以根据文件所处的相对位置对文件进行定位
当改变绝对路径而不改变文件相对位置时对路径没有影响
"""
print("---------------------")
# eg：在当前文件找到module_module01.py文件的绝对路径
file_path = os.path.join(os.getcwd(), "module_module", "module_module01.py")
print(file_path)

"""
获取一个目录文件夹下所有文件或者目录的的名称
这个功能可以获取每个文件的绝对路径
"""
name_list = os.listdir(os.getcwd())
print(name_list)

# eg：找到这个文件夹下的所有的.py文件的绝对路径
# 列表推导式
file_path_list = [os.path.join(os.getcwd(), i)
                  for i in os.listdir(os.getcwd())
                  if i.endswith(".py")]
print(file_path_list)

"""
判断文件类型的方法
"""
print("---------------------")
path = r"D:\PycharmProjects\pythonProject\PythonClass\class38.py"
# 判断是不是文件
print(os.path.isfile(path))
# 判断是不是文件夹
print(os.path.isdir(path))
# 获取目录下的所有文件夹
file_path_list01 = [os.path.join(os.getcwd(), i)
                    for i in os.listdir(os.getcwd())
                    if os.path.isdir(os.path.join(os.getcwd(), i))]
print(file_path_list01)

"""
判断路径/目录是否存在
"""
print("---------------------")
print(os.path.exists(path))
print(os.path.exists('D:\\PycharmProjects\\pythonProject\\PythonClass\\module01.py'))





"""
创建文件夹
"""

print("---------------------")
# path = 'D:\\PycharmProjects\\pythonProject\\PythonClass\\class38_demo'
# print(os.path.exists(path))
# os.mkdir(path)  # 在该路径上创建文件夹

# 创建多层级的文件夹
# path = 'D:\\PycharmProjects\\pythonProject\\PythonClass\\class38_demo\\demo'
# print(os.path.exists(path))
# os.makedirs(path)

"""
删除文件 
"""
# 删除文件
# os.remove()
# 删除文件夹 -- 只能删除空文件夹
# os.rmdir("class38_demo\\demo")  # 删除多层级的文件夹
# os.removedirs()  # 也可以

"""
拆分路径

    字符串前面的"r"表示原始字符串。
    这意味着字符串中的所有字符都是字面意思，没有特殊的转义序列。
"""

path = r"D:\PycharmProjects\pythonProject\PythonClass\class33.py"
print(os.path.split(path))



