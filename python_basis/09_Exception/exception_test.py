# 异常的捕获
# 异常的基本语法
try:
    pass # 代码块1
except:
    pass # 代码块2

# 异常捕捉
def exception(param):
    i = 0
    try:
        len1 = len(param)
        while i<len1:
            print(param.popitem())
            i+=1
    except:
            print('传递的参数必须为字典类型')

exception({1:'H',2:'B'})
exception([1,2,3,4])
# (2, 'B')
# (1, 'H')
# 传递的参数必须为字典类型

# 带finally子句的异常处理
# 语法格式
try:
    pass
except:
    pass
finally:
    pass
# finally下面的代码块不管是否出错都会被执行
try:
    1/0
except:
    print('除数不能是0')
finally:
    print('程序执行到finally')
# 除数不能是0
# 程序执行到finally

# 异常信息统计
# ValueError 对象值不正确
# IndexError 下标元素不存在时出现的错误
# NameError  指定的对象名不存在
# KeyError   字典的键不存在
# TypeError  类型错误
# ModuleNoFoundError 模块文件找不到
# SyntaxError  语法无效
# AttributeError 对象属性，方法引用，赋值不当
try:
    i+=1
except NameError:
    print('变量未进行初始化定义')
    # 变量未进行初始化定义
# raise 自己触发异常
i = '1'
if type(i)!=int:
    raise TypeError('参数类型错误')
# Traceback (most recent call last):
#   File "c:\py_vscod\python_project\python_basis\09_Exception\tempCodeRunnerFile.py", line 3, in <module>
#     raise TypeError('参数类型错误')
# TypeError: 参数类型错误