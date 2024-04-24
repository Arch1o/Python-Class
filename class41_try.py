"""
异常处理机制
    为了不让异常影响程序的正常运行，一般需要进异常捕获处理，
    用的是try/except/finally语句

try：
    待执行的代码块
except Exception as e:
    print(e)
"""

print("111")
try:
    print(1/0)
# 捕获错误信息
except Exception as e:
    print(e)
print("222")


list01 = [1, 2, 3]
try:
    print(list01[4])
# 捕获特定错误
except IndexError as e:
    print(e)

"""
打开某一个文件，如果出现异常，将异常信息文件记录到一个“记录文件”中
"""
try:
    with open("test.txt03","r", encoding="utf-8") as file:
        print(file.readline())
except Exception as e:
    print(e)
    print(type(e))
    with open("exception.txt", "w", encoding="utf-8") as w:
        w.write(str(e))

"""
else
    没有异常的时候执行的操作
    
finally:
    不管有没有异常都执行操作
"""

print("-----------------------")
try:
    file = open("test.txt","r")
except Exception as e:
    print(e)
else:
    file.close()
    print("成功对file进行close")
# 和直接放在外面执行是一样的
finally:
    print("不管有没有异常都会执行的代码块")
print("没有finally，不管有没有异常都会执行的代码块")
