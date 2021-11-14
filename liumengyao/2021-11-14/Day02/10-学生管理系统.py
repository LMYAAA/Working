"""
1、欢迎界面
    1
    2
    3
    4
    5
2、1是添加学生
    通过input输入添加
    添加到对象里（列表、字典、集合）进行保存
    每个对象是一个学生信息，总的所有对象要保存在（集合里 ）
3、2是查看学生
    集合里面有没有学生的对象信息
    如果有，那就遍历展示
    如果没有，那就提示没有信息，退出
4、3是修改学生信息
    集合里面有没有学生的对象信息
    如果有
        可以通过学号来定位查找学生，
        学号怎么来？  通过input进行输入
        再进行更改
    如果没有
        需要提示没有信息，返回
5、4是删除学生信息
    集合里面有没有学生的对象信息
    如果有
        可以通过学号来定位查找学生，
        学号怎么来？  通过input进行输入
        在进行删除
    如果没有
        需要提示没有信息，返回
6、5是退出系统
    直接结束程序就OK了

"""

# 学生保存的对象
class Student:
    def __init__(self, name, age, userid):
        self.name = name
        self.age = age
        self.userid = userid



# 针对学生管理的增删改查
class StudentManage():

    def __init__(self):
        # 创建保存学生对象的 容器
        self.data = set()

    def showStudent(self):
        # 查看学生信息
        if self.data:
            for stu in self.data:
                print( "{}\t\t\t{}\t\t\t{}".format(stu.name, stu.age, stu.userid)   )
        else:
            print('当前系统中没有学生信息，需要先添加再进行操作！')


    def addStudent(self):
        # 添加学生信息
        name = input('请输入学生姓名：')
        age = input('请输入学生年龄：')
        uid = input('请输入学生学号：')
        # 创建学生对象
        stu = Student(name, age,  uid)
        # 通过set集合，添加学生信息
        self.data.add(stu)


    def updateStudent(self):
        # 修改学生信息
        if self.data:
            uid = input('请输入学生学号:')
            for stu in self.data:
                if uid == stu.userid:
                    stu.name = input('请输入学生姓名:')
                    stu.age = input('请输入学生年龄:')

    # 删除学生信息
    def deleteStudent(self):
        if self.data:
            uid = input('请输入学生学号:')
            for stu in self.data:
                if uid == stu.userid:
                    self.data.remove(stu)
                    break
        else:
            print('无学生信息')

    def run(self):
        # 启动入口
        while True:
            print('欢迎来到学生管理系统')
            print('1、添加学生信息。')
            print('2、查看学生信息。')
            print('3、修改学生信息。')
            print('4、删除学生信息。')
            print('5、退出系统。')
            num = input('请输入你要进行操作:')
            print( num )
            if  num == '1':
                print('添加学生')
                self.addStudent()
            elif num == '2':
                print('查看学生')
                self.showStudent()
            elif num == '3':
                print('修改学生')
                self.updateStudent()
            elif num == '4':
                print('删除学生')
                self.deleteStudent()
            else:
                print('退出系统')
                break
                # return


sm = StudentManage()
sm.run()