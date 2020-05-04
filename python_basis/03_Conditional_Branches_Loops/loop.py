# 循环语句while循环
i = 0
while i < 3:
    i += 1
    print(i)
# 1
# 2
# 3
# while循环嵌套语句
i, j = 0, 3
while i < 3:
    while i < j:
        print((i+1)*j)
        j -= 1
        i += 1
# 3
# 4
# for循环
name = 'this, is, mis, spring'
i = 0
for strName in name:
    if strName == 's':
        i = i+1
        print(i)
# 1
# 2
# 3
# 4
# 利用内建范围函数range实现for循环
for i in range(19):
    if i % 2 == 0:
        print('%d是偶数' % (i))
# 0是偶数
# 2是偶数
# 4是偶数
# 6是偶数
# 8是偶数
# 10是偶数
# 12是偶数
# 14是偶数
# 16是偶数
# 18是偶数
# 循环控制语句break，终止跳出循环
str_user = 'how are you'
for i in range(len(str_user)):
    print('for循环%d次' % (i+1))
    if str_user[i:i+3] == 'how':
        print('how is %d' % (i))
        break
    print('for是否执行这句代码')
# for循环1次
# how is 0
# ------continue语句是控制循环方向，当满足条件之后contioue回到循环开始处进行下一次的循环
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print('%d是偶数' % (i))
# 2是偶数
# 4是偶数
# 6是偶数
# 8是偶数
