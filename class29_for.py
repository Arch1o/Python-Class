## 循环语句（二）
# for循环
for i in 'abcd':
    print(i)
    # i = string[0] ,遍历/迭代过程
    # i = string[1]
    # i = string[2]
    # i = string[3]

list1 = [(1,2), (3,4), (5,6)]
# 序列赋值/解包
for i, j in list1:
    print(i,j)

for i in [1, 2, 3, 4]:
    print(i)
    if i > 2:
        break  # 阻止所在的循环
else:
    print(5)

# for循环写99乘法表（比while更加简便）
for right in range(1, 10):
    for left in range(1, right+1):
        print(f'{left}×{right} = {left*right}', end=" \t")
    print() # 换行

# pass语句，是一个用于临时占完占位的空语句
for i in [1,2]:
    pass # 此时电脑不会报错

# 迭代器 enumerate（iterable，star=0）将元素和索引打包成元组
print(list(enumerate(['a', 'b', 'c']))) # [(0,'a'), (1, 'b'), (2, 'c')]

for i in enumerate(['a', 'b', 'c'], 100):
    print(i)
for index, item in enumerate(['a', 'b', 'c'], 100):
    print(index, item) # 分别得到索引和元素

# 不知道为什么有bug 死循环
'''a = 1
while a <= 5:
    
    if a == 3:
        a += 1
        continue    

print(a)
a += 1
'''
# 优化一下 石头剪刀布游戏（玩一把执行一次太麻烦 用死循环）
import random
info={0:'石头',1:'剪刀',2:'布'}
while True:
    computer=random.randint(0,2)
    '''print(computer)'''
    player=int(input('请公主出拳: 0代表石头, 1代表剪刀, 2代表布:'))
    print(f'电脑出拳:{info[computer]}')
    print(f'玩家出拳:{info[player]}')
#判断胜负
    if computer == player:
        print('平局！')
    elif computer-player == 1 or computer-player == -2:
        print('玩家胜！')
    else:
        print('电脑胜利！')
# 停止游戏
    if input('请问是否需要继续游戏Y/N:') in ('N', 'n'):
        print('游戏结束，欢迎下次光临...')
    break
