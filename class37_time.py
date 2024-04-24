"""
time 模块
"""
import sys

# dir() 函数
# 如果对象是一个模块。则返回这一指定模块内所定义的函数、类与向量列表。

import module01

print(dir(module01))
print(module01.__doc__)  # 脚本头部的文档说明

md = module01.ModuleDemo(name="md")
print(dir(md))
print(module01.ModuleDemo.__doc__)

"""
Python的标准模块：
sys模块：提供了与Python解释器交互的函数和变量，用于操控Python的运行环境
random模块：用于生成随机数
os模块：提供访问操作系统服务的功能
time模块：提供了处理时间的函数
calender模块：提供了处理年历和月历的方法
详情参考： 
"""
# http www.cnbolgs.com/ribavnu/p/4886472.html

# sys.exit()  # 执行到当前行退出程序的执行

import random

random.seed(1)  # 保证每一次随机数不变 固定随机出来的随机数据
print(random.random())  # 生成0-1之间的随机浮点数
print(random.randint(1, 10))

list01 = [1, 2, 3, 4, 5]
result = random.sample(list01, 3)  # 随机采样3个数据
print(result)

"""
time模块
"""
import time

# 获取当前的时间戳
time_stamp = time.time()
print(time_stamp)  # 从1970年到现时刻经过的闰秒数

# 计算程序用时（秒）
print('--------------------')
start = time.time()
for i in range(1000):
    print(i, end=" ")
    if i >= 999:
        print(i)  # 换行

print(time.time() - start)

# 获取当前时间
time02 = time.ctime()
print(type(time02))

# 计算格林尼治时间
time03 = time.gmtime()
print(time03)
print(type(time03))

# 计算当地使时间
time04 = time.localtime()
print(time04)
print("-------------------------")
print(time04.tm_hour)  # 获取时间对象
time.sleep(1)  # 等待1秒

# 时间格式化输出 xxxx/xx/xx xx：xx：xx
"""
    %Y 年份
    %m 阿拉伯数字月份
    %d 日期
    %H 小时（24）
    %I 小时（12）
    %p （AM/PM）
    %M 分钟
    %S 秒
    %Z 时区
    %A %a 英文星期
    %B %b 英文月份
"""
time05 = time.strftime("%Y/%m/%d %H:%M:%S %p %z %A %a %B %b", time04)
print(time05)
print(time.strftime("%Y/%m/%d %H:%M:%S"))  # 默认输出当前时间

# 将字符串转换成时间格式的数据

# str01 = "2022/10/15 16:01:25"
# time06 = time.strftime(str01, "%Y/%m/%d %H:%M:%S")
# print("-------------------------")
# print(time06)
# print(type(time06))
"""
不知道为什么会报错
"""
print("-------------------------")
import datetime
str01 = "2022/10/15 16:01:25"
time06 = datetime.datetime.strptime(str01, "%Y/%m/%d %H:%M:%S")
print(time06)
print(type(time06))
