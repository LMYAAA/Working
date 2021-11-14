"""
分支结构
    if 条件表达式:
        代码块1...
    else:
        代码块2...

    注意:
    (1) 条件表达式只返回两个值: True、False
    (2) True: 正数、负数, 不包含0, 其他的所有不为空的字符串、字典等等
    (3) False: 0、None、null、其他所有为空的字符串、列表等等
"""
print('---大于小于---')
a = 1
if a < 2:
    print('正确')  # 1 < 2
else:
    print('错误')

print('---非空字符串、列表---')
if [0]:
    print('正确')  # 因为是非空列表 所以正确
else:
    print('错误')

print('--- and ---')
if 1 < 2 and 3 < 2:
    print('正确')
else:
    print('错误')

print('--- or ---')
if [] or [0]:
    print('正确')
else:
    print('错误')

print('--- not ---')
if not [] :
    print('正确')
else:
    print('错误')



"""
多重判断
if 条件表达式:
    代码块
elif 条件表达式:
    代码块
elif 条件表达式:
    代码块
else:
    代码块
"""
print('-----多重判断-----')
if False:
    print('第一条件表达正确')
elif True:
    print('第二条件表达正确')
elif True:
    print('第三条件表达正确')
else:
    print('错误')


"""
嵌套
"""
print('-----嵌套-----')
a = 5
b = 10
if a<b and a%10 <=50:
    a += 10
    b *= 5
    if a == b:
        print('正确')
    else:
        print('错误')
        