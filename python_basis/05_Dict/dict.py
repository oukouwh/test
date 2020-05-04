# 字典(Dict)是可变的无序集合，同时是以键值对为基本元素存储各种数据类型的集合
# 使用大括号{}表示字典的开始和结束，元素之间用逗号(,)进行分割
# 键值对是由键(Key)和值(Value)组成，中间用冒号:进行分隔。
# 字典属于一对一映射关系数据类型
# 字典的基本格式
dict_test = {1: 'tom', 2: 'jack'}
print(len(dict_test))  # 2
print(dict_test)  # {1: 'tom', 2: 'jack'}
# 字典要求键的唯一性
dict_key = {'1': 'java', '2': 'c++', '2': 'c#'}
print(len(dict_key))  # 2
print(dict_key)  # {'1': 'java', '2': 'c#'}
# 字典只保留了键相同的最后一个元素
# 字典操作的基本方法
# 利用赋值给字典增加元素
dict_in = {1: 'haha', 2: 'heihei'}
dict_in[4] = 'hehe'
print(dict_in)  # {1: 'haha', 2: 'heihei', 4: 'hehe'}
# setdefault   当字典中键不存在时，设置键值对；当键存在时，获取键对应的值
dict_set = {1: 'hhhh', 2: 'fff'}
dict_set.setdefault('dddd')  # 未指定的值，默认为None
dict_set.setdefault('Taobao', '淘宝')
print(dict_set)  # {1: 'hhhh', 2: 'fff', 'dddd': None, 'Taobao': '淘宝'}
# 字典值的查找
# 字典名+key进行查找
dict_select = {1: 'hello', 2: 'world', 3: 'python'}
print(dict_select[1])  # hello
# get       根据指定键，返回对应值；访问键不存在时，返回None
print(dict_select.get(2))  # world
# 字典值的修改
# 利用赋值修改键对应的值
dict_modify = {'python': 1, 'java': 2, 'c++': 3}
dict_modify['c++'] = 4
print(dict_modify)  # {'python': 1, 'java': 2, 'c++': 4}
# update    利用一个字典更新另外一个字典
dict_up = {'java': 'A', 'Python': 'B', 'GO': 'C'}
dict_up1 = {'java': 'J'}
dict_up.update(dict_up1)
print(dict_up)  # {'java': 'J', 'Python': 'B', 'GO': 'C'}
# 字典元素的删除
# 利用del函数进行删除
dict_del = {'hello': 'A', 'world': 'B', 'python': 'C'}
print(dict_del)  # {'hello': 'A', 'world': 'B', 'python': 'C'}
del(dict_del['hello'])
print(dict_del)  # {'world': 'B', 'python': 'C'}
# pop      删除指定键的元素，返回指定键对应的值
dict_pop = {'hello': 'A', 'world': 'B', 'python': 'C'}
pop_value = dict_pop.pop('hello')
print(pop_value)  # A
print(dict_pop)  # {'world': 'B', 'python': 'C'}
# popitem   随机返回元素，并删除元素
dict_popitem = {'hello': 'A', 'world': 'B', 'python': 'C'}
print(dict_popitem)  # {'hello': 'A', 'world': 'B', 'python': 'C'}
key1, value1 = dict_popitem.popitem()
print(key1, value1)  # python C
print(dict_popitem)  # {'hello': 'A', 'world': 'B'}
# 字典的遍历操作
# items     以元组数组的形式返回字典中的元素
dict_items = {'hello': 'A', 'world': 'B', 'python': 'C'}
for i in dict_items.items():
    print(i)
# ('hello', 'A')
# ('world', 'B')
# ('python', 'C')
# dict_items([('hello', 'A'), ('world', 'B'), ('python', 'C')])
print(dict_items.items())
# 遍历所有的键
dict_items = {'hello': 'A', 'world': 'B', 'python': 'C'}
for i in dict_items:
    print(i)
# hello
# world
# python
# keys      以可以浏览的类似列表形式返回指点中的键
dict_items = {'hello': 'A', 'world': 'B', 'python': 'C'}
for i in dict_items.keys():
    print(i)
# hello
# world
# python
# 遍历所有的值
dict_items = {'hello': 'A', 'world': 'B', 'python': 'C'}
for i in dict_items:
    print(dict_items[i])
# A
# B
# C
# values    返回字典中的值
dict_items = {'hello': 'A', 'world': 'B', 'python': 'C'}
for i in dict_items.values():
    print(i)
# A
# B
# C
# 字典其他操作
# in成员操作
dict_items = {'hello': 'A', 'world': 'B', 'python': 'C'}
if 'hello' in dict_items.keys():
    print('hhahhah')  # hhahhah
else:
    print('ERROR')
dict_items = {'hello': 'A', 'world': 'B', 'python': 'C'}
if 'A' in dict_items.values():
    print('hhahhah')  # hhahhah
else:
    print('ERROR')
# clear     字典清空
dict_clear = {'hello': 'A', 'world': 'B', 'python': 'C'}
print(dict_clear)  # {'hello': 'A', 'world': 'B', 'python': 'C'}
dict_clear.clear()
print(dict_clear)  # {}
# copy      复制生成另外一个字典
dict_copy = {'hello': 'A', 'world': 'B', 'python':  'C'}
dict_copy1 = dict_copy.copy()
print(dict_copy)  # {'hello': 'A', 'world': 'B', 'python': 'C'}
print(id(dict_copy))  # 2289195167000
print(dict_copy1)  # {'hello': 'A', 'world': 'B', 'python': 'C'}
print(id(dict_copy))  # 2289195167000
# fromkeys  使用给定的键建立新的字典，每个键默认对应的值为None
dict_frmkey = {}.fromkeys([1, 2, 3])
print(dict_frmkey)  # {1: None, 2: None, 3: None}
# 字典嵌套
user = {'tom': 13, 'jack': 34, 'alex': 43}
count = {'hhh': 99.8, 'EE': 87, 'SE': 109.8}
userInfo = {'user': user, 'count': count}
print(userInfo)
# {'user': {'tom': 13, 'jack': 34, 'alex': 43}, 'count': {'hhh': 99.8, 'EE': 87, 'SE': 109.8}}
# 列表嵌入字典
list_user = [1,2,34,5]
list_password = ['aaaa', 'bbbb', 'cccc']
list_dict = {'user':list_user, 'password':list_password}
print(list_dict)
# {'user': [1, 2, 34, 5], 'password': ['aaaa', 'bbbb', 'cccc']}
# 字典嵌入列表
no_one = {'A':100, 'B':120, 'C':399}
no_two = {'C':999, 'D':399.9, 'E':1999}
no_three = {'F':10000.9, 'G':12999, 'H':99999.9 }
dict_list = [no_one,no_two,no_three]
print(dict_list)
# [{'A': 100, 'B': 120, 'C': 399}, {'C': 999, 'D': 399.9, 'E': 1999}, {'F': 10000.9, 'G': 12999, 'H': 99999.9}]
i = 0 # 循环控制变量初始值
count_money = 0 # 消费金额初始化
list_count = len(dict_list) # 获取list的元素个数
dict_init = {} # 定义空的字典变量
sum1 = 0 # 消费总额初始化
while i < list_count:
    dict_init = dict_list[i]
    sum1 = sum(dict_init.values()) # 获取消费金额求和
    count_money+=sum1
    print(dict_init)
    print('第%d桌消费%.2f元'%(i+1,sum1))
    i+=1
# {'A': 100, 'B': 120, 'C': 399}
# 第1桌消费619.00元
# {'C': 999, 'D': 399.9, 'E': 1999}
# 第2桌消费3397.90元
# {'F': 10000.9, 'G': 12999, 'H': 99999.9}
# 第3桌消费122999.80元