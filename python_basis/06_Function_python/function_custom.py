# 自定义函数。
# 位置参数
def userInfo(name, age):
    print('姓名%s,年龄%d'%(name,age))

userInfo('A',19)
# 姓名A,年龄19

userInfo(19, 'B') 
# 参数类型不一致，传入需要对照确认传入的参数类型是否能够对应
# TypeError: %d format: a number is required, not str