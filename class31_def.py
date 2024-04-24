##  函数01
# 定义函数
def fun01(input_list):
    input_list[0] = 2
    print(input_list)

list01 = [1, 2, 3]
print(list01)  # [1, 2, 3]
fun01(list01)  # [2, 2, 3]
print(list01)  # [2, 2, 3]

print('=============================')

def fun02(imput_str):
    imput_str = "aaaa"
    print(imput_str)

str01 = "abc"
print(str01) # abc
fun02(str01) # aaaa
print(str01) # abc

# 原因：注意列表为可变对象，字符串不可变

# 变量的作用域
n_2 = 10  # 全局变量

def func01(n):
    # print(n_2)  # 报错
    n_2 = n*2        # 局部变量
    print(n_2)
func01(3)
# 函数内部定义的变量在函数外部不可以使用
# 函数外部定义的变量在函数内部可以使用，但会先在函数内部找，不能发生冲突


