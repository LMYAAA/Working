"""
类、对象/实例、 实例化
类: 类别、物以聚类。有相同属性、相同行为的事物统称为类
对象:  在类中的一个具体事例称为对象
实例化:  从类生成到对象的一个过程

定义类
    class 自定义名称():
        定义属性
        定义行为(类方法、函数)

"""
# 创建一个学生类
class Student():
    # 定义属性
    name = ""
    age = 0
    userid = ""
    #定义行为
    def eat(self):
        # self  谁掉用这个方法，谁就是self
        # 1、zhangsan调用了eat方法
        # 2、zhangsan 就是这个 self
        # 3、zhangsan 有  name属性、age属性、eat方法
        # 4、self？ 有没有这些方法呢
        # 5、self也有name属性、age属性、eat方法
        print(self.name, '正在吃饭')
        self.sleep()

    def sleep(self):
        print(self.name, '正在休息')

#创建对象
zhangsan = Student()
# 对象访问属性
# 对象名.属性名
zhangsan.name = '张三'
zhangsan.age = 20
zhangsan.userid = "007"
print( zhangsan.name )

#对象访问行为方法
# 对象名.方法名()   记得要加括号， 不加括号意思为查看一些方法信息
print(  zhangsan.eat  )
zhangsan.eat()


#创建第二个对象
lisi = Student()
lisi.name = '李四'
lisi.age = 18
lisi.userid = "001"
lisi.eat()