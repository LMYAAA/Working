"""
初始化方法（构造方法）
    运行类的第一个启动的方法 就是初始化方法
    即使我们没有写初始化方法，也会默认 继承object类中的初始化方法
"""
#创建类
class Student(object):

    def __init__(self, names, age, userid):
        print('我是一个初始化方法')
        # 在类里面构造属性
        self.name = names

    def eat(self):
        print('正在吃饭')



#调用类创建对象
zhangsan  = Student( '张三', 20, "007" )
print( zhangsan.name )
