# 变量是指在计算机编程中与关联的标识符配对的内存存储位置，在使用相关类型的值，其值可以被修改
# Python变量被使用将会在内存中产生两个动作；
#   1.开辟指定地址的空间
#   2.赋予指定的变量值
#   在python中变量的指定同时，需要强制赋初始值否则编译器报错。
# python中允许同时为多个变量进行赋值
a = b = c = 0
print(a, b, c)
# 0 0 0
# 变量值的类型
# Python中基本变量的类型 字符串(Strin) 数字(Numeric) 列表(List) 元组(Tuple) 字典(Dictionary) 五种数据类型、
# ----------String数据类型字符串--------------
# 字符串(String)由任意字节的字符组成，用单引号' 双引号" 三引号''' 成对表示
name = 'aaaa'
name1 = "bbbb"
name2 = '''cccc'''
print(name, name1, name2)
user, user1, user2 = 'user', "user1", '''user2'''   # 多个变量进行赋值
print(user, user1, user2)
# aaaa bbbb cccc
# user user1 user2
# ----字符串基本操作---
# ----字符串的读取-----
strName = 'This is String'  # 字符串的每个字符对应一个下标，可以通过下表读取数据
print(strName[0])  # T
print(strName[1])  # h
#  ----切片[左下标:右下标]
print(strName[1:4])
#  his 切片范围是1<= x < 4
# 带冒号省略下标方式切片[:6] 等同于[0:6]
print(strName[:6])
#  This i
# 读取整个字符串[:]
print(strName[:])
#  This is String
# 带步长读取切片[左下标:右下标:步长]
print(strName[::2])
#  Ti sSrn
# 负数下标的读取，用负数下标从右向左读取字符串
print(strName[-1])
#  g
# 从右向左读取倒数第五个第四个第三个第二个第一个字符串
print(strName[-5:-1])
# trin
# -------字符串的拼接通过+来实现
strUser = 'userName'
strPassword = 'password'
userInfo = strUser + strPassword
print(userInfo)
# userNamepassword
# --------字符串值的修改
name = 'this is date'
new_name = name[:8] + 'data'
print(new_name)
#  this is data
# ------字符串的删除，整个字符串的删除可以使用del，注意，删除完成后再次调用会报错
delName = 'delete'
print(delName) # delete
del(delName)
# print('ERROR'+delName) # NameError: name 'delName' is not defined  错误信息
# -----获取字符串的长度 len
print(len(name)) # 12
# ------原始字符串控制符号r/R
# 字符串里含有特殊意义的转义符，\b \n 在没有使用r的情况下\b转为退格符，实现退一格效果
print('c:\back\str') # c:ack\str
print(r'c:\back\str') # c:\back\str
# -------重复输出字符串 *
print('he' * 2) # hehe
# 格式化字符串(%)
age = 22
print('my age is %d'%age) # my age is 22



