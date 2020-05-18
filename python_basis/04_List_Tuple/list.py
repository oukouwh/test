# 列表List是python语言中的一种数据结构，是可变的序列，也是一种可以存储各种数据类型的集合
# 用[]表示列表的开始和结束，元素之间用逗号(,)进行分割。每个元素对应一个下标。
# 列表的基本格式
# 定义一个空列表
print([])  # []
print(len([]))  # 查询列表的长度 0
# 定义一个带有一个元素的列表
print([233])  # [233]
print(len([233]))  # 1
# 定义两个元素的列表变量
print([123, 456])  # [123, 456]
print(len([123, 456]))  # 2
# 根据下标读取列表中的数据
data_list = ['123', 456, '上海', 90]
print(data_list)  # ['123', 456, '上海', 90]
print(data_list[0])  # 123
print(data_list[1])  # 456
print(data_list[2])  # 上海
print(data_list[3])  # 90
print(data_list[4])  # IndexError: list index out of range
# 列表的基本操作
# append    在列表尾部增加元素
list_user = ['JackMa', 'Tom', 'Elliot', 34, 44]
list_user.append('New String')
print(list_user)  # ['JackMa', 'Tom', 'Elliot', 34, 44, 'New String']
# insert    在指定位置插入新的元素
list_insert = [1, 2, 4, 5, 6]
list_insert.insert(2, 3)
print(list_insert)  # [1, 2, 3, 4, 5, 6]
# index     返回指定元素的下标
list_index = ['hello', 111, 3, 'world']
print(list_index.index(111))  # 1
# in成员运算判断，判断元素是否存在于列表中
list_in = [123, 456, 789]
print('a' in list_in)  # False
print(123 in list_in)  # True
# 用下标读取对应元素
list_idx = [123, 456, 789, 345]
print(list_idx[2])  # 789
# 切片读取元素
print(list_idx[1:])  # [456, 789, 345]
# 列表元素的修改
list_up = ['this', 'is', 'tom']
list_up[2] = 'jack'
print(list_up)  # ['this', 'is', 'jack']
# clear     列表清空
list_clear = ['123', 'haha', 'hello']
print(list_clear)  # ['123', 'haha', 'hello']
print(len(list_clear))  # 3
list_clear.clear()
print(list_clear)  # []
print(len(list_clear))  # 0
# pop       删除并返回指定下标对应的元素
list_pop = ['1', 2, 4, 'del']
list_pop.pop()  # 未指定删除坐标，默认删除最后一位
print(list_pop)  # ['1', 2, 4]
list_pop.pop(0)
print(list_pop)  # [2, 4]
# remove    删除列表中指定元素 当列表中有重复的元素时remove只会删除左边的第一个元素
list_remove = ['1', 4, '2', 3, 4]
print(list_remove)  # ['1', 4, '2', 3, 4]
list_remove.remove(4)
print(list_remove)  # ['1', '2', 3, 4]
# del函数 可以删除整个列表对象，也可以删除指定元素
list_del = ['12', '23', '34', '45']
del(list_del[0])
print(list_del)  # ['23', '34', '45']
list_del2 = ['12', '23', '34', '45']
del list_del2
print(list_del2)  # NameError: name 'list_del2' is not defined
# extend    两个列表元素合并
list_ex1 = [1, 2, 3]
print(id(list_ex1))  # 1445885596232 地址未发生变化
list_ex2 = ['jack', 'alex', 'jon']
list_ex1.extend(list_ex2)
print(list_ex1)  # [1, 2, 3, 'jack', 'alex', 'jon']
print(id(list_ex1))  # 1445885596232
# 使用 + 拼接
list_ex1 = [1, 2, 3]
print(id(list_ex1))  # 1832056869448 地址发生变化
list_ex2 = ['jack', 'alex', 'jon']
list_ex1 = list_ex1 + list_ex2
print(list_ex1)  # [1, 2, 3, 'jack', 'alex', 'jon']
print(id(list_ex1))  # 1832057434312 两次结果地址不一样
# sort      对列表元素进行排序
list_sort = [1, 3, 6, 99, 2, 67]
list_sort.sort()
print(list_sort)  # [1, 2, 3, 6, 67, 99]
# copy      复制生成另一个列表
list_copy = ['123', 2222]
print(id(list_copy))  # 1899999220296
new_list_copy = list_copy.copy()
print(id(new_list_copy))  # 1899999220808
new_list_copy_address = new_list_copy
print(id(new_list_copy_address))  # 2997930972232
# count     统计指定元素个数
list_count = [1, 2, 1, 33, 1, 5, 6]
print(list_count.count(1))  # 3
# reverse   反转列表元素顺序
# 数字的reverse
list_reverse = [3, 4, 6, 1, 7, 99, 110]
print(list_reverse)  # [3, 4, 6, 1, 7, 99, 110]
list_reverse.reverse()
print(list_reverse)  # [110, 99, 7, 1, 6, 4, 3]
# 字符串的reverse
str_reverse = ['Tom', 'jack', 'python', 'c++']
print(str_reverse)  # ['Tom', 'jack', 'python', 'c++']
str_reverse.reverse()
print(str_reverse)  # ['c++', 'python', 'jack', 'Tom']

list_result = []
while True:
    str_input = input('请输入字符串')
    if str_input == '':
        break
    list_result.append(str_input)

str_result = ''.join(list_result)
print(str_result)
print(type(str_result))

# 反转
str_demo = 'hello world'
list_result = str_demo.split(" ")
print(list_result)
print(type(list_result))
str_result = ' '.join(list_result[::-1])
print(str_result)

list_num = [99, 2, 34, 5, 67, 8]
min_value = list_num[0]
for i in range(1, len(list_num)):
    if min_value > list_num[i]:
        min_value = list_num[i]

print(min_value)

# 列表推导式
list_num = [1, 2, 3, 4, 5]
list_num1 = []
for i in list_num:
    list_num1.append(i + 1)
# print(list_num1)
# [2, 3, 4, 5, 6]

# 列表推导式简化版
list_num1 = [i + 1 for i in list_num]
print(list_num1)  # 结果同上面运行结果一致，代码看着更优雅
# [2, 3, 4, 5, 6]


# 列表推导式1
list_num = [11, 22, 33, 44, 56]
list_num1 = []
for i in list_num:
    if i > 30:
        list_num1.append(i)
print(list_num1)
# [33, 44, 56]

# 列表推导式简化版
list_num1 = [i for i in list_num if i > 30]
print(list_num1)  # 结果同上面运行结果一致，代码看着更优雅
# [33, 44, 56]

list_num = [i ** 2 for i in range(1,11)]
print(list_num)
list_num1 = [i for i in list_num if i % 2 == 1]
print(list_num1)
list_num2 = [i for i in list_num if i % 2 == 0]
print(list_num2)
