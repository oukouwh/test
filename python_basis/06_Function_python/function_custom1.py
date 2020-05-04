# 关键字传递参数,主要避免参数传递出现混乱，无需考虑参数的位置顺序
def userInfo(name,age):
    print('姓名%s,年龄%d'%(name,age))

userInfo(name='HAHA',age=19)
# 姓名HAHA,年龄19
userInfo(age=19,name='HEHE')
# 姓名HEHE,年龄19

# 默认值传参
def fun_default(name='',age=20):
    print('姓名%s,年龄%d'%(name,age))

fun_default(10) # 姓名10,年龄20
fun_default() # 姓名,年龄20
fun_default('jack',23) # 姓名jack,年龄23


# 不定长参数*，**
# 使用格式 函数名([param1,param2,.....]*paramX)
# 传递任意数量的参数值
# 带*paramX参数进行传递的时候，只能放置在最右边的参数中，否则自定义函数的时候会报错
def fun_many_param(name,*params):
    print(name) # A
    print(type(params)) # <class 'tuple'>
    print(params) # ('type', 'string', 'int')

fun_many_param('A','type','string','int')

# 传递任意数量的键值对
# 使用格式 函数名([param1,param2,.....]**paramX)
# **paramX 传递的是键值对
def fun_many_param_key_values(name,**params):
    print(name) # AAA
    print(type(params)) # <class 'dict'>
    print(params) # {'TEST': 'BBB', 'COLOR': '红色'}

fun_many_param_key_values('AAA', TEST='BBB', COLOR='红色')

# 传递元组，列表，字典值
# 传递元组
def fun_param_tuple(name,params):
    print(name) # 对A
    print(type(params)) # <class 'tuple'>
    print(params) # ('小', '平', '要不起')

fun_param_tuple('对A',('小','平','要不起'))


def fun_param_list(name,params):
    print(name) # 对A
    print(type(params)) # <class 'list'>
    print(params) # ['小', '平', '要不起']

fun_param_list('对A',['小','平','要不起'])

def fun_param_dict(name,params):
    print(name) # 对A
    print(type(params)) # <class 'dict'>
    print(params) # {'A': '小', '上海机场': '平', 'AA': '要不起'}

fun_param_dict('对A',{'A':'小','上海机场':'平','AA':'要不起'})

