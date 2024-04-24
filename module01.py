"""
class35 中的自定义模块
"""
def p_moudule():
    print("我是module01中的方法")

class ModuleDemo():
    """
    说明
    """
    def __init__(self, name):
        self.name = name

    def p_module(self):
        print("我是module01模块里面ModuleDemo类中的方法p_module")

print("我是module01模块")

if __name__ == '__main__':  # 私有化代码 只有在执行当前脚本的时候执行，其他脚本import时不会执行
    print("我也是module01模块的私有化代码")

