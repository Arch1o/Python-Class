"""
作业：
    模拟一个加单的银行进行业务的办理
    类：
        创建一个银行类
    属性：
        一个属于银行的类属性
            用来存储所用银行的开户信息，包含卡号、密码、用户名、余额
            （外界不能随意访问修改，开户时要进行卡号验证，查看卡号是否存在）
        每个对象拥有：
            卡号、密码、用户名、余额
            （外界不能随意访问修改）
    方法：
        银行类拥有
            查看银行的开户总数
            查看所有用户的个人信息（包含卡号、密码、用户名、余额）
        每个对象拥有
            实例化对象时候传入相关参数
                初始化对象积累属性
            取钱（需要输入卡号和密码验证）
            存钱（需要输入卡号和密码验证）
            查看个人信息（需要输入卡号和密码验证）
"""


class BankAccount:
    # 类属性：私有属性
    __user = {}

    # 每个对象拥有卡号、密码、用户名、余额
    def __init__(self, cardId, pwd, name, balance):
        # 查看卡号是否存在
        if cardId not in BankAccount.__user.keys():
            # 若卡号不存在，在银行的类属性中添加一个用户信息
            # 以cardId作为键。该字典包含三个键值对：'pwd'对应密码（pwd），'Username'对应用户名（name），'Balance'对应余额（balance）
            # {cardId： {'pwd': pwd, 'Username': name, 'Balance': balance}}
            BankAccount.__user[cardId] = {'pwd': pwd, 'Username': name, 'Balance': balance}
            self.__cardId = cardId
            self.__pwd = pwd
            self.__name = name
            self.__balance = balance
        else:
            # 验证
            if BankAccount.__user[cardId]['Username'] == name and BankAccount.__user[cardId]['pwd'] == pwd:
                self.__cardId = cardId
                self.__pwd = pwd
                self.__name = name
                self.__balance = balance
            else:
                print("账号或者密码错误")

    # 查看本银行的开户总数
    @classmethod
    def userscount(cls):
        print(f"开户总数: {len(cls.__user)}")

    # 查看所有用户的个人信息
    @classmethod
    def userinfo(cls):
        for key, val in cls.__user.items():
            name = val['Username']
            pwd = val['pwd']
            balance = val['Balance']
            print(f'卡号: {key}\n用户名: {name}\n密码: {pwd}\n余额'
                  f': {balance}\n', '============================')

    # 取钱
    def withdraw(self, cardId, currentPwd, num):
        # if cardId == self.__cardId:
        #     if currentPwd == self.__pwd:
        #         if num <= self.__balance:
        #             self.__balance -= num
        #             # 需要对类属性同时更新
        #             BankAccount.__user[cardId]["Balance"] -= num
        #             print(f'{self.__name}取钱成功')
        #         else:
        #             print('余额不足')
        #     else:
        #         print('密码错误')
        # else:
        #     print('卡号错误')

        # 换成更简洁 清晰的格式：
        if cardId not in BankAccount.__user:
            print('卡号错误')
            return

        if BankAccount.__user[cardId]['pwd'] != currentPwd:
            print('密码错误')
            return

        if BankAccount.__user[cardId]['Balance'] <= num:
            print('余额不足')
            return

    # 存钱
    def deposit(self, cardId, currentPwd, num):
        if cardId == self.__cardId:
            if currentPwd == self.__pwd:
                self.__balance += num
                # 需要对类属性同时更新
                BankAccount.__user[cardId]["Balance"] += num
                print(f'{self.__name}存钱成功')
            else:
                print('密码错误')
        else:
            print('卡号错误')

    def viewinfo(self):
        print(f'卡号: {self.__cardId}\n用户名: {self.__name}\n密码: {self.__pwd}\n余额'
              f': {self.__balance}')


# 测试
huangshuchen = BankAccount('0001', 123456, 'hsc', 100)
zhangsan = BankAccount('0002', 123456, '张三', 100)

BankAccount.userscount()
BankAccount.userinfo()

huangshuchen.withdraw('0001', 123456, 50)
huangshuchen.deposit('0001', 123456, 200)


zhangsan.deposit('0002', 123456, 20)
zhangsan.withdraw('0002', 123456, 250)
print(zhangsan._BankAccount__balance)

