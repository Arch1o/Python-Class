"""
35 模块
"""
# 模块与包
'''
Python 模块 是一个py文件，模块是在函数和类的基础上，将一系列代码组织
到一起的集合体。一般所有的模块在Python文件的开头部分导入，并按照以下顺序：
1 Python标准模块库
2 Python第三方模块
3 应用程序自定义模块
'''
# form ... import ... 从模块中调用某个功能

# 导入自定义的模块module01
from PythonClass import module01

# 使用module01中的方法
module01.p_moudule()

print("============================")
# 第二种使用module中方法的方式
from PythonClass.module01 import p_moudule
p_moudule()

# 使用module01中类的方法
# 实例化类 => 和普通的面向对象编程方法一样
m1 = module01.ModuleDemo(name="m1")
print(m1.name)
m1.p_module()

"""
模块/包/函数方法名字/变量名字 尽量不要出现冲突（与原有的函数或模块重复）
"""



