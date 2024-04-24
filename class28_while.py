## 循环语句（一）
# while 循环
"""格式"""
num = 1
while num < 100:
    print(num, end=" ")
    num += 1  # num = num + 1
print('===========================')

#求1-100间的整数的和
num2 = 1
total = 0
while num2 <= 100:
    total += num2
    num2 += 1
print(total)
print('===========================')

# while Ture循环（死循环/无限循环）
while True:
    print('hello world')
    break # 配合控制语句限制循环次数

# while...else,与if...else的区别是后者存在互斥关系
print('===========================')

# while嵌套循环
'构件99乘法表'
right = 1
while right < 10:
      
    left = 1
    while left <= right:
        print(f'{left}×{right} = {left*right}', end=" \t")  # \t代表水平制表符
        left += 1
    print()  # 换行

    right += 1


