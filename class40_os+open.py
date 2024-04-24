"""
os+open
"""
import os
import random
import time
import sys

"""
新建三个文件夹：
    grade7，grade8，grade9
每个年级的文件夹创建三个文件：
    class1、class2、class3
每一个班级的文件夹中创建两种文件：
    student_info.txt：姓名、学号、性别、年龄。。。
    student_score.txt：学号、每一科目的成绩
    每一行是一个学生的数据，每个字段用 ；隔开
"""
# 学号
num = 1
# 定义姓名生成方法
x_list = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王"]
m_list = ["浩宇", "宇浩", "达", "晓希", "家辉", "爱国", "涛", "晨"]


def gen_name():
    x = random.sample(x_list, 1)[0]  # 返回的是含有1个随机元素的列表 所以要加[0] 索引出所包含的元素
    m = random.sample(m_list, 1)[0]
    return x + m


"""
遍历创建文件夹
"""

start = time.time()
for grade in ['grade7', 'grade8', 'grade9']:
    for class_name in ['class1', 'class2', 'class3']:

        class_dir_path = os.path.join(os.getcwd(), 'class40', grade, class_name)  # 路径拼接
        print(class_dir_path)
        if not os.path.exists(class_dir_path):
            os.makedirs(class_dir_path)  # 创建文件路径

        num_list = []  # 每次循环到这里 num list为空列表 但num一直在增加

        # 创建info文件
        student_info_path = os.path.join(class_dir_path, 'student_info.txt')
        # 以"w"模式打开会自动创建上述路径:
        with open(student_info_path, "w", encoding="utf-8") as w:
            w.write("学生姓名;学生学号;性别;年龄\n")  # 每次写入的数据会覆盖
            for i in range(5):
                num_list.append(num)
                student_name = gen_name()
                # 性别随机生成
                student_gender = random.sample(["男", "女"], 1)[0]
                # 年龄随机生成
                student_age = random.randint(12, 16)
                w.write("{};{};{};{};\n".format(student_name, num, student_gender, student_age))
                num += 1

        # 创建成绩文件
        student_score_path = os.path.join(class_dir_path, 'student_score.txt')
        with open(student_score_path, "w", encoding="utf-8") as w:  # 这里的w不会重复，因为退出上一个with open后，上一个w就被释放了
            w.write("学号;语文;英语;数学\n")
            # 保证学生的学号不变
            for i in num_list:
                w.write("{};{},{},{}\n".format(i, random.randint(60, 100), random.randint(60, 100),
                                               random.randint(60, 100)))
        print(num_list)
print(time.time() - start)


"""
作业：依照我们生成的数据：
    对每个班级学生平均年龄做统计，返回一个dict
    每个学生的三科成绩的平均分，返回一个dict
    每个班级每一科成绩的平均分，dict
"""
print('----------------------作业-------------------------')
# 获取文件路径
grade_list = os.listdir(os.path.join(os.getcwd(), 'class40'))
print(grade_list)  # ['grade7', 'grade8', 'grade9']

student_info_path_list = []
student_score_path_list = []

# 遍历
for grade in grade_list:
    print(grade)
    class_list = os.listdir(os.path.join(os.getcwd(), 'class40', grade))
    print(class_list)

    for class_name in class_list:
        class_dir_path = os.path.join(os.getcwd(), 'class40', grade, class_name)
        student_info_path_list.append(os.path.join(os.getcwd(), 'class40', grade, class_name, 'student_info.txt'))
        student_score_path_list.append(os.path.join(os.getcwd(), 'class40', grade, class_name, 'student_score.txt'))

print(student_info_path_list)
print(student_score_path_list)

# 每个班级平均年龄
age_avg_lsit = []
for path in student_info_path_list:
    with open(path, 'r', encoding='utf-8') as w:
        next(w)  # 跳过第一行
        res = w.readlines()
        print(res)

pass

