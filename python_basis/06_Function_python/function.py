# 函数Function，通过指定的代码实现特定功能，具有相对独立性，可以让其他代码进行调用
# 函数定义的基本语法
# def 函数名([参数]):
#   函数体
#   return 返回值
# 不带参数案例
def prt_hello():
    print('hello')

prt_hello()
# hello
# 带参数
def sum_num(nums):
    i = 10
    print(i + nums)

sum_num(10)
# 20
# 返回值retun
def fun_return(num):
    i = 100
    return i + num

print(fun_return(23))
# 123