"""
正则表达式/元字符
"""
import re

"""
常见的单字符的匹配
    匹配任意一个单字符（/n /r除外）：    
        []匹配[]列举出来的其中一个字符
        [^]匹配非[]列出来的其中要给字符
        . 匹配一个单字符
        ...
        
常见的表示匹配数量的元字符
    对前面匹配到的单字符进行数量限制
    * 0-无限次
    + 1-无限次
    ？ 0-1次
    {m} m次
    {m，} 至少m次
    {m，n} m-n次
    https://blog.csdn.net/ZYC88888/article/details/98479629
    ...
    
表示匹配边界的元字符
    ^ 以某某开始 区别开[^]
    $ 以某某结尾
    ...
"""

str01 = "abcd1234@!,\n\r"
result01 = re.match(".", str01)
print(result01)

result01 = re.match(".*", str01)
print(result01)

result01 = re.match(".{4}", str01)
print(result01)

"""
匹配一个qq号 5-12位 传数字组合 且第一位不能为0 
"""

print("------------------------")
str02 = '153312435555'
print(len(str02))
result02 = re.match("[1-9][0-9]{4,11}$", str02)
print(result02)
# "[1-9]"表示匹配任意一个1到9之间的数字。
# "[0-9]{4,11}"表示匹配任意一个0到9之间的数字，且这样的数字连续出现4到11次。
# "$"表示字符串的结束。

"""
对输入的手机号进行校验
    开头为137、138、158、181、139、136、133、152、188
    11位
"""

print("------------------------")
phone_num = '13301263386'
result03 = re.match("(137|138|158|181|139|136|133|152|188)[0-9]{8}", phone_num)
print(result03)
# "(137|138|158|181|139|136|133|152|188)"表示匹配任意一个在括号内的电话号码前缀。
# "[0-9]{8}"表示匹配任意一个0到9之间的数字，且这样的数字连续出现8次。

"""
找出下列所有.py的文件
找出所有图片格式的文件
"""

print("------------------------")
str03 = "a.py, b.txt, c.png, d.jpg, e.py, a_01.py, a_py"
result04 = re.findall("\w+\.py", str03)
print(result04)
# "\w+"表示匹配任意一个或多个字母、数字或下划线。
# ".py"表示匹配字符串".py"。

result05 = re.finditer("\w+\.(png|jpg|gif)", str03)  # 使用findall只返分组括号里面的结果
for i in result05:
    print(i)

result05 = re.findall("(\w+\.)(png|jpg|gif)", str03)
print(result05)

"""
找出所有时间   
"""

print("------------------------")
str04 = "今天是2022年10月16，明天是2022-10-17，昨天是2022/10/15，1999年5月1号，123456789"
result06 = re.findall("[0-9]{4}.[0-9]{1,2}.[0-9]{1,2}", str04)  # 没有校验功能
# ['2022年10月16', '2022-10-17', '2022/10/15', '1999年5月1', '123456789']
print(result06)
# 可以改进

"""
通过正则进行数据清洗
    将文本中的汉字、英文单词提取出来；符号、数字替换成空格
    \u4e00-\u9fa5 中文的编码范围
"""

print("------------------------")
str05 = "将本文数据中的汉字、英文&单词提取string出来；123，？符号、数字替换成python中文的编码范围"
result07 = re.sub("[^\u4e00-\u9fa5A-Za-z0-9]+", " ", str05)
print(result07)
# "[^\u4e00-\u9fa5A-Za-z0-9]"表示匹配任意一个不在中文字符、英文字母和数字范围内的字符。
# "+"表示匹配前面的字符一次或多次。
# " "表示空格。