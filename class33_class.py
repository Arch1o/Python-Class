## 面向对象
# 类：具有相同属性和方法的对象集合
# 构造方法，类方法，静态方法
class 类名称():
    '''
    文档说明
    '''


class Student:
    '''
    这是一个学生类
    '''
    student = "我是一个学生类"  # 类属性 对于实例化过后的对象都具有类属性

    def __init__(self, name, age, class_name, grade_name):
        # 构造方法 实例化时会自动调用
        # self不是关键字参数，是表达的是当前的对象

        # self.name 为实例属性，通过形参接收到的值赋值给实例属性
        # name是形参
        self.name = name
        self.age = age
        self.class_name = class_name
        self.grade_name = grade_name

    def introduction(self, aihao):
        '''
        自我介绍的功能，介绍：姓名、年龄、年级、班级、爱好
        '''
        print("我叫{}，今年{}岁，来自{}-{}，喜欢{}".format(self.name, self.age, self.grade_name, self.class_name, aihao))
        return "我叫{}，今年{}岁，来自{}-{}，喜欢{}".format(self.name, self.age, self.grade_name, self.class_name, aihao)
        print("我叫{}，今年{}岁，来自{}-{}，喜欢{}".format(self.name, self.age, self.grade_name, self.class_name, aihao))
        # return后def已经结束 无法再print出

    def pname(self):
        print("姓名：{}".format(self.name))

    @staticmethod  # 静态方法 可以不需要使用self，意味着在该方法中无法访问到实例属性
    def pp():
        # 但可以访问类属性
        print(Student.student)  # 类名.类属性

    @staticmethod
    def add_func01(x, y):  # 不是静态方法，必须实例化后才能使用
        print(x + y)

    def add_func02(self, x, y):  # 不是静态方法，必须实例化后才能使用
        print(x + y)


'''
练习：定义一个学生类
类属性 grade_count：统计每个年级学生数量 字典
静态方法：新增学生add_student；修改类属性grade_count
普通方法：自我介绍
'''


class Student02:
    grade_count = 0

    def __init__(self, name, age, class_name, grade_name, score):
        self.name = name
        self.age = age
        self.class_name = class_name
        self.grade_name = grade_name
        # 定义私有属性Score
        self.__score = score

    @staticmethod  # 静态方法放在class外面也可以 为了代码规范性class里
    def add_student():
        Student02.grade_count += 1  # 访问类属性：通过类名来访问呢

    def intro(self, hobby):
        print(f"大家好，我叫{self.name}，今年{self.age}岁，来自{self.grade_name},{self.class_name}，喜欢{hobby}")

    @classmethod  # 类方法 等价于可以访问类本身的普通函数方法
    def student_out(cls):
        """
          @classmethod 是 Python 中的一个装饰器，用于将一个方法定义为类方法。
          类方法与普通方法的区别在于，类方法的第一个参数是类本身（通常命名为 cls），而不是类的实例。
          这意味着类方法可以在不创建类实例的情况下调用，也可以被子类继承和重写。
          """
        """
        这是一个类方法
        """
        cls.student = "我是一个学生类，通过类方法修改后的学生类"


# 实例化对象
zhangsan = Student(name="张三",
                   age="15",
                   class_name="二班",
                   grade_name="八年级")

lisi = Student(name="李四",
               age="14",
               class_name="三班",
               grade_name="八年级")

# 获取实例对象的属性  实例对象名.实例属性名
print(zhangsan.name)
print(zhangsan.age)
print(zhangsan.grade_name)
print(zhangsan.class_name)

print(lisi.name)
print(lisi.age)
print(lisi.grade_name)
print(lisi.class_name)

# 实例对象调用类属性
print(zhangsan.student)
print(lisi.student)
# 没有实例对象时，类也可以调用类属性
print(Student.student)
# 实例对象的属性 只能由实例对象访问

print("-----------------------")
# 调用类方法
zs_zwjs = zhangsan.introduction("篮球")
ls_zwjs = lisi.introduction("乒乓球")
print(zs_zwjs)
print(ls_zwjs)

# 调用类方法pname（打印名字）
print("-----------------------")
zhangsan.pname()  # 调用方法括号必须要加
print(zhangsan.pname)  # panme是方法而不是属性
print("-----------------------")
print(zhangsan.pname())  # None 因为没有return 默认的return是none

# 调用静态方法
print("-----------------------")
Student.pp()
zhangsan.pp()

Student.add_func01(1, 2)
zhangsan.add_func01(1, 2)
print("-----------------------")
zhangsan.add_func02(1, 2)
Student.add_func02(zhangsan, 1, 2)  # 未实例化的对象无法访问

print("=======================")
# 练习
zhangsan = Student02('zhangsan', '15', '八年级', '二班', score='80')
zhangsan.intro('篮球')
zhangsan.add_student()
print(Student02.grade_count)

# 类方法的调用
Student02.student_out()  # 类可以调用类方法
zhangsan.student_out()  # 实例对象也可以调用类方法
print("-----------------------")
print(Student02.student)
print(zhangsan.student)

# 访问呢私有属性： _类名__属性名
print(zhangsan._Student02__score)  # 强制访问
