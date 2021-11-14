"""
切割
2021-11-14
"""
print('------切割------')
# 1.切片方式提取
str1 = "2021-11-14"
y = str1[0:4]
m = str1[5:7]
d = str1[-2:]
print( '切片获得到的day: ' + d )

# 2.split
# str.split()    #返回的是列表
res = str1.split('-')
print(res)         # ['2021', '11', '14']
print(type(res))   # <class 'list'>

str2 = "9:57:10"
print(str2.split(':'))



"""
去除首尾空格
"""
print('------去除首尾空格------')
str3 = "   hello world    "
print(str3)

# 1. str.strip() 去除两边空格
res1 = str3.strip()
print(res1)

# 2. str.lstrip()  去除左边空格
res2 = str3.lstrip()
print(res2)

# 3. str.rstrip()  去除右边空格
res3 = str3.rstrip()
print(res3)


"""
替换
replace( 定位到替换的位置, 替换成什么 )  
"""
print('------替换------')
str4 = "我是: XXX"
print(str4)
res = str4.replace('XXX', '张三').replace('我', '你')
print(res)

str5 = "   hello world    "
res5 = str5.replace(' ', '')   # 定位的是所有的空格
print(res5)

res5 = str5.replace('l', 'X')   # 定位的是所有的空格
print(res5)


"""
格式化输出
    %s  传递转化成字符串
    %d  传递转化成整数 (只取整, 不进行四舍五入)
    %f  传递转化成小数 (默认保留六位, 后边的进行四舍五入) (%.2f 保留两位)
"""
print('------格式化输出------')
str6_s = "我是: %s"
print(str6_s)
print(str6_s % '法外狂徒·张三')
print(str6_s % '尼古拉斯·赵四')
print(str6_s % ['生活有判头'])

str6_d = "我的薪资是: %d"
print(str6_d)
print(str6_d % 1000)
print(str6_d % 999.9)

str6_f = "我的房间面积是: %f 平米"
print(str6_f)
print(str6_f % 150)
print(str6_f % 150.23)
print(str6_f % 150.123456789)

str6_Xf = "我的房间面积是: %.2f 平米"
print(str6_Xf % 150.123456789)



"""
format
"""
print('------format------')
str7 = "我是:{}, 我在:{}, 我喜欢:{}"
print(str7)
print(str7.format('李四', '河南', '跑步'))