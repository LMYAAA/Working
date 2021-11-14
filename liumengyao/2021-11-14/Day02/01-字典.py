"""
1.字典
    <class 'dict'>
    写法: { key : value , key : value }
    解释: 键值对的形式, 中间用逗号隔开
    注意: 字典是一个特殊的容器
         key 是唯一的 (如果重复 以最后一个为准)
         value 可以存储任意类型
"""

# 1.创建字典
# (1) 方法一
dict_1 = dict()
print(type(dict_1))
# (2) 方法二
dict_2 = {}
# (3) 创建非空字典
dict_3 = {"name":"小鲁班", "武器":"大炮", 100:[1, 2, 3]}
# dict_3 = {"name":"小鲁班", "武器":"大炮", 100:[1, 2, 3], "name":"卤蛋"}
print(dict_3)


# 2.查找
# (1) 把 key 可以当成索引下标
print(dict_3['name'])
# 查找不存在的key时 会因为查找不到而报错 (KeyError: '要查找的key值')
# print((dict_3['hobby']))   # KeyError: 'hobby'


# 3.更改
# 首先需要确定字典中有这个 key, 再赋值就是更改 value
dict_3[100] = '123'
print(dict_3)


# 4.添加
# 字典中没有这个 key, 再赋值就是添加键值对
dict_3['hobby'] = '上王者'
print(dict_3)


# 5.删除
# (1) del
del dict_3[100]
print(dict_3)

# (2) 删除整个字典
# del dict_3

# (3) clear() 清除dict中所有键值对
# dict_3.clear()
# print(dict_3)


# 6.获取所有的 key
res = dict_3.keys()   # 返回的是一个可迭代对象
res = list(res)       # 可迭代对象可以转化成列表
print(res[0])


# 7.获取所有的 value
all_value = dict_3.values()
print(all_value)        # dict_values(['小鲁班', '大炮', '上王者'])
print(type(all_value))  # <class 'dict_values'>


# 8.获取所有的 key 和 value
all_item = dict_3.items()  # 返回的格式: dict_items([('':''),('':'')])
print(all_item)        # dict_items([('name', '小鲁班'), ('武器', '大炮'), ('hobby', '上王者')])
print(type(all_item))  # <class 'dict_items'>




