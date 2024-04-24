"""
加载/写入 文件
"""
import pandas as pd
import json

a = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                  "B": ["B0", "B1", "B2", "B3"],
                  "C1": ["C0", "C1", "C2", "C3"],
                  "D2": ["D0", "D1", "D2", "D3"]}, index=[0, 1, 2, 3])
print(a)

# 存储
a.to_csv(r"class60/a1.csv")
# 去掉索引
a.to_csv(r"class60/a2.csv", index=False)
# 设置分隔符号+改表头
a.to_csv(r"class60/a3.csv", index=False, sep=";", header=['a', 'b', 'c', 'd'])
# 去掉表头
a.to_csv(r"class60/a4.csv", index=False, sep=";", header=False)

# 读取
print("==============读取=================")
a01 =pd.read_csv(r"class60/a2.csv")
print(a01)
print(type(a01))

"""
json文件
    dict类型
"""

# df存储为json
a.to_json('class60/a1.json')
# 读取
print("==============json=================")
a_json = pd.read_json('class60/a1.json')
print(a_json)

dict01 = {"a": [1, 2, 3],
          "b": [3, 4, 5]}
dict_json = json.dumps(dict01, ensure_ascii=False)
print(type(dict_json))  # <class 'str'>

with open("class60/dict_json.json", "w", encoding="utf-8") as w:
    w.write(dict_json)

b = pd.read_json("class60/dict_json.json")  # 文件必须是df格式才能可读
print(b)
print("==============excel=================")
a.to_excel("class60/a.xlsx", index=False)
a_xlsx = pd.read_excel("class60/a.xlsx")
print(a_xlsx)
