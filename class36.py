"""
包： 模块打包后的集合
"""
import module01

module01.p_moudule()
from module_module.module_module01 import pp
pp()

import sys
# 查看当前环境变量中存在的路径
print(sys.path)

# 绝对路径 从根目录开始找

# 相对路径 从当前路径开始找 ./ ==> 退出一级  ../ ==>退两级
