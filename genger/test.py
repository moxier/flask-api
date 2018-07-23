"""
    Created by Amirk on 2018-07-22.
"""


class Foo:
    name = 'Amirk'
    age = 22

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ('name', 'age', 'gender')

    def __getitem__(self, item):
        return getattr(self, item)


f = Foo()

# 将类中的实例变量转为字典
# 但是 __dict__不能将类当中的类变量进行转换
# print(f.__dict__)  # {'gender': 'male'}


# 使用dict 将类中的类变量,实例变量转为字典
# 当程序执行到 dict(f) 的时候
# 程序首先会到类中访问 keys 函数
# keys 函数中返回了我们想返回的一个属性名称, 保存为一个序列
# 然后程序会再去访问类中的 __gititem__  函数
# 将 keys 函数返回的序列中的属性名称, 依次传入 __gititem__ 中进行 访问, 返回需要的值
print(dict(f))
