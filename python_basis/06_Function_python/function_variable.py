# 函数的全局变量和局部变量
j = 10
def fun_variable(i):
    i = i+ j 
    return i
i = 4
print('j的值为%d,是全局变量，i的值为%d是局部变量'%(j,fun_variable(3)))
print('函数外的i的值%d新的变量而非函数内部的i'%(i))
# j的值为10,是全局变量，i的值为13是局部变量
# 函数外的i的值4新的变量而非函数内部的i

# global 关键字
# 函数内部默认只能读取全局变量的值，若需要修改全局变量，需要使用global关键字进行事先声明，否则在函数
# 内部修改全局变量会英文报错
j = 10
print('全局变量j的地址%d'%id(j))
i = 20
def test():
    global j # 声明j为全局变量
    j = j+5
    i = 34
    return i
print('局部变量i的值为%d,全局变量i的值为%d'%(test(),i))
print('全局变量j的值%d,函数赋值之后的地址为%d'%(j,id(j)))
# 全局变量j的地址140733928993312
# 局部变量i的值为34,全局变量i的值为20
# 全局变量j的值15,函数赋值之后的地址为140733928993472


# 闭包(Closure) 闭包是介于全局变量和局部变量之间的特殊变量。
j = 13
def clo_fun():
    i = 3 # 闭包变量
    def clo_fun1():
        a = j + i
        return a 
    return clo_fun1()

print('调用带有闭包变量的函数clo_fun()执行结果%d'%(clo_fun()))
# 调用带有闭包变量的函数clo_fun()执行结果16
# 全局变量，局部变量，闭包变量之间的关系
# 全局变量>闭包变量>局部变量

# 匿名函数
# python中使用lambda创建匿名函数，匿名函数没有函数名称
lambda x,y:x*y
a = lambda x,y:x*y
print(a) # <function <lambda> at 0x000001DEA03AA438>
a(3,5)
print(a(3,5))
# 15


