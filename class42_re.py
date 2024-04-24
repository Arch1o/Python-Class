"""
Python正则表达式
    通过re模块实现
"""
import re

"""
re.compile()  # 编译正则表达式，生成了一个正则表达式对象，可以用match、search等方法使用
match 只能从字符串的第一个位置开始匹配（检查/校验），且只能匹配到一个
"""

str01 = "pythonjavahadoopspark"
# 匹配出python => compile+match
pat01 = re.compile("python")  # 正则表达式对象
result = pat01.match(str01)  # 匹配成功，则返回匹配对象。不成功，则返回None
print(result)  # object <re.Match object; span=(0, 6), match='python'>
# 取出结果
print(result.span())
print(result.start())
print(result.end())
print(result.group())

"""
直接使用re.match
"""

print('--------------------')
result02 = re.match("python", str01)
print(result02)

"""
re.search
扫描整个字符串，返回匹配成功的第一个对象。无法匹配成功返回None
(检查/校验)待检测字符串中是否有我们想要的对象
"""

print('--------------------')
# 方式一
str02 = "aaaapythonjavahadoopspark"
pat02 = re.compile("python")
result03 = pat02.search(str02)
print(result03)

# 方式二
result03 = re.search("python", str02)
print(result03)
print(result03.span())

"""
re.findall
    在整个字符串中查找，返回一个列表。
    没有对象返回空列表
re.finditer
    在整个字符串中找到所有对象，返回一个迭代器，每个迭代结果都是一个match对象。
    匹配不到返回空迭代器。
"""

print('--------------------')
ste03 = "aaaapythonjavahadoopsparkpython02"
result04 = re.findall("python", ste03)
print(result04)

result05 = re.finditer("python", ste03)
print(result05)  # 迭代器
# print(next(result05))
# print(next(result05))
for i in result05:
    print(i)

"""
re.split
    按照匹配规则将能够匹配到的字符串作为分隔符对字符串进行分割，返回一个列表
"""

print('--------------------')
str04 = "name;age;;score"
pat03 = re.compile(";+")  # ";+"为一种正则表达式，后续学习
result06 = pat03.split(str04)
print(result06)

result07 = re.split(";+", str04)
print(result07)
# 等价于字符串的split对象方法
print(str04.split(";"))

"""
re.sub
    用于替换指定的字符串
"""
print('--------------------')
str04 = "name;age;;score"
pat04 = re.compile(";+")
result08 = pat04.sub("===", str04)
print(result08)