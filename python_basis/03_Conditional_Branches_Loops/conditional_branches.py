# if条件分支
# if的基本语法
# 单分支判断
if True:
    print('hello')  # hello
if False:
    print('false')  # 条件不成立未进行输出
# 双分支判断
if True:
    print('yes')  # yes
else:
    print('no')
if 2 > 5:
    print('2>5')
else:
    print('条件不成立')  # 条件不成立
# 多条件分支判断
a = 'hello'
if a =='yes':
    print('yes')
elif a =='no':
    print('no')
else:
    print('a等于' + a)  # a等于hello

