# Python语言中的数字和数学语言中的数字是一样的，数字可以分为：
# 整数(Integer)
# 浮点数(Float)
# 复数(Complex)
# 布尔(Boolean)
# 算术运算符号
# + - * / % ** //
print(1+2)  # 加法运算 3
print(2-1)  # 减法运算 1
print(2*2)  # 乘法运算 4
print(6/2)  # 除法运算 3.0
print(8 % 3)  # 取模返回余数 2
print(5**4)  # 幂返回x的y次幂 625
print(9//4)  # 取整数，返回商的整数部分 2
# 整数(Integer) ,是有正整数负整数和 0组成，不包括小数和分数
num1 = 3
num2 = 9
sum_num = num1 + num2
print('整数相加的和为：%d' % (sum_num))
print('整数减法的值为：%d' % (num2 - num1))
print('整数乘法的积为：%d' % (num1*num2))
print('整数除法的商为: %d' % (num2/num1))
result = (num1+num2)*(num2-num1)/6
print('加减乘除混合运算结果：%d' % result)
# 浮点数，在python中浮点数是带小数点的数字，因此浮点数不一定是精确值
print(10.0/3)  # 3.3333333333333335
# 复数(Complex),复数是由实部和虚部组成，数学表现形式为a+bj 其中a为实部b为虚部 j为虚数单位，bj称为虚数
print((1-4j)*(2-3j))  # (-10-11j)
# 布尔(Boolean)布尔类型的数据结果为True或者False，用于逻辑判断
print(True and False)  # False
print(True and True)  # True
print(True or False)  # True
print(not False)  # True
# ----------比较运算符-------------
#  === != > < >= <=
# ===运算符
a = 2
b = 2
print(a == b) # True
print(a != b) # False
print(a < b) # False
print(a > b) # False
print(a >= b) # True
print(a <= b) # True
# -------数据类型转换
print(int(3.2)) # 3
print(int('23')) # 23
# ---转换成浮点类型float
print(float(10)) # 10.0
# -----转换为复数complex
print(complex(2,5)) # (2+5j)
# -----转换为字符串
print(str(complex(4,5))) # (4+5j)

