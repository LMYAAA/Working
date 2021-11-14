"""
循环
"""
"""
1.for循环
    for 自定义变量 in 可迭代对象:
        循环体
"""

print('-------for循环-------')
list_1 = ['周一', '周二', '周三', '周四', '周五', '周六']
for i in list_1:
    print( i )


"""
2.while循环
    while 条件表达式:
        循环体
        结束语句
        
        注意:
            结束语句是为了控制表达式是true 还是false
"""
print('-------while循环-------')
a = 1
while a < 10:
    print(a)
    a += 1


"""
break :  跳出整个循环
continue :  结束当前循环, 直接进入下一次循环
"""
print('------- break || continue -------')
print('--- break ---')
list_2 = ['周一', '周二', '周三', '周四', '周五', '周六']
for i in list_2:
    print( i )
    if i == '周三':
        break

print('--- continue ---')
a = 1
while a < 10:
    print(a)
    if a == 5 or a > 5:
        break
    a += 1

print('--- 不打印 三 四 ---')
list_3 = ['周一', '周二', '周三', '周四', '周五', '周六']
for i in list_3:
    if i == '周三' or i == '周四':
        continue
    print(i)

print('--- 只打印 五 六 ---')
a = 1
while a < 10:
    a += 1
    if a < 5 or a > 6:
        continue
    print(a)
