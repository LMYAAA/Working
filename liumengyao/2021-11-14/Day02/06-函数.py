"""
函数
    (1) 用过哪些函数
        sort()
        print()
        input()
        type()
        len()

    (2) 什么是函数
        有特定功能、完成指定任务的一段代码块

    (3) 为什么使用函数
        i. 可以隐藏代码的实现
        ii. 提高代码的复用性
        iii. 提高代码的可读性、可维护性

    (4) 函数的定义
        def 自定义变量名( 参数1, 函数2...):
            函数体
            return

    (5) 参数
        形参: 形式上的参数, 并没有实际的意义，也可以称之为占位符
        实参: 实际的参数值, 在调用函数地方出现

    (6) 传递参数的方法
        位置传递: 按照位置的先后顺序进行传递参数
        关键字传递: 再调用的地方，传递变量值，通过变量名称取定义函数地方找寻，
                  看有没有相对应的关键字，如果没有，则会报错
                  如果有这个关键字，那么会把这个变量赋值给这个关键字

    (7) return
        返回一个值:   默认这个值是什么类型，就返回什么类型
        返回多个值:   默认是元组类型
        自定义返回值: 自定义设定返回类型
"""

# 创建加法函数功能
def addition(a, b):
    # 使用参数 a 加上 参数 b 得出结果赋值给 c 这个变量
    c = a + b
    return c

# 调用函数
print('传入参数')
res_1 = addition(10, 20)
print(res_1)

res_2 = addition(b=30, a=50)
print(type(res_2))
print(res_2)

res_3 = addition(['hello'], ['world'])
print(type(res_3))
print(res_3)