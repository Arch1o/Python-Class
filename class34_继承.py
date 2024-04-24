"""
34 继承
"""


# 继承：如：一个dog类型的对象派生自animal类
# 多态： 类的不同表现出不同的行为
# 封装性：
# 当我们定义一个class的时候，路从现有的class中继承

class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def p_eat(self):
        print(f"{self.name}喜欢吃{self.food}")


animal01 = Animal(name="动物1", food="肉")


# 声明了一个Dog子类继承Animal父类
class Dog(Animal):
    def __init__(self, name, food, play):
        # 不需要单独构造父类中已有的属性
        # 加载父类的构造函数方法
        super(Dog, self).__init__(name=name, food=food)
        self.play = play

    def p_play(self):
        print(f"{self.name}喜欢玩{self.play}")


if __name__ == '__main__':  # 以下的代码是私有化的代码
    dog01 = Dog(name="哈巴狗", food="骨头", play="飞盘")
    # 实例化对象直接使用继承父类的属性
    print(dog01.name)
    # 子类可以直接继承父类的方法
    dog01.p_eat()

    # 子类构造属于自己的属性和方法 Ps:父类不能使用子类的方法
    print(dog01.play)
    dog01.p_play()

    # 对继承的父类方法修改 如Cat子类继承Animal


class Cat(Animal):
    def __init__(self, name, food, drink):
        super(Cat, self).__init__(name, food)
        self.drink = drink

    # 对父类的方法进行重构
    def p_eat(self):
        print(f"{self.name}喜欢吃{self.food}，喜欢喝{self.drink}")


cat01 = Cat(name="小花", food="鱼", drink="水")
cat01.p_eat()
print("--对比重构后的方法与父类的方法--")
animal01.p_eat()

# 调用重构前的父类方法
super(Cat, cat01).p_eat()  # 使用super调用子类重构前的父类的方法

"""
练习：
构造父类：People 属性：姓名，年龄 方法：自我介绍（构建类的时候建议使用大驼峰命名法，构建函数的时候使用小驼峰命名法）
子类：Student 属性：姓名，年龄，年纪，班级，考试成绩 方法：自我介绍/输出考试成绩
"""

print('---------------------------')


class People:
    """
    这是一个人类类 作为当前的父类
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'我叫{self.name}，我今年{self.age}岁')


zhangsan = People(name="张三", age="20")
zhangsan.intro()


class Student(People):
    """
    这是一个学生类 是父类People的子类
    """

    def __init__(self, name, age, grade_name, class_name, score):
        super(Student, self).__init__(name=name, age=age)  # 继承People类的属性
        self.grade_name = grade_name
        self.class_name = class_name
        self.score = score

    def intro(self):
        print(f"我叫{self.name}，今年{self.age}岁，来自{self.grade_name}-{self.class_name}，成绩为{self.score}分")


# 创建实例
lisi = Student(name="李四", age="15", grade_name="九年级", class_name="六班", score="80")
# 调用重构后的方法
lisi.intro()
# 输出lisi的成绩
print(lisi.score)
# 调用重构前父类的方法
super(Student, lisi).intro()

"""
多重继承
class xxx（Base1，Base2，Base3）
"""


class A:
    def __init__(self, a):
        self.a = a

    def pa(self):
        print("我是A类里面的a方法，我的属性：{}".format(self.a))


class B:
    def __init__(self, b):
        self.b = b

    def pb(self):
        print("我是B类里面的b方法，我的属性是：{}".format(self.b))


class C(A, B):
    """
    C类继承了A/B两个父类
    """

    def __init__(self, a, b, c):
        # 通过这种方式继承父类时 默认只能继承前一个
        # super(C, self).__init__(a=a, b=b) 报错
        # 使用基于类名的继承方法
        A.__init__(self, a=a)
        B.__init__(self, b=b)
        self.c = c

    def pc(self):
        print("我是C类里面的c方法，我自己的属性是：{}".format(self.c))


if __name__ == '__main__':
    c01 = C(a="aaa", b="bbb", c="ccc")
    print(c01.a)
    print(c01.b)
    print(c01.c)
    c01.pa()
    c01.pb()
    c01.pc()
    # 使用子类的实例对象调用父类的方法
    super(C, c01).pa()  # 该方法没有指定父类是谁，在继承多个父类时，会默认调用左边的




