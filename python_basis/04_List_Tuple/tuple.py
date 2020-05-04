# 元组的基本操作 Tuple
# 元组是不可变的序列，可以存储各种数据类型的集合，用()表示，之间用逗号分隔
tuple_test = (123,'hello', 345, '332')
print(tuple_test) # (123, 'hello', 345, '332')
print(type(tuple_test)) # <class 'tuple'>
# 元组的基本操作方法
# count 统计指定元素个数
tuple_count = (1, 3, 4, 5, 7, 76, 3 , 3, 3, 3)
print(tuple_count.count(3)) # 5
# index 返回指定元素的下标
print(tuple_count.index(4)) # 2
# 元组操作的内置函数
# len 统计元组元素个数
print(len(tuple_count))  # 10
# max 返回元组中最大值的元素
print(max(tuple_count))  # 76
# min 返回元组中最小值的元素
print(min(tuple_count))  # 1
# tuple 将列表转换为元组
tuple_name = tuple([1,2,3,4])
print(tuple_name) # (1, 2, 3, 4)
# 将元组转换成列表
tuple_list = (123, 999)
print(type(tuple_list)) # <class 'tuple'>
list_tuple = list(tuple_list)
print(list_tuple) # [123, 999]
print(type(list_tuple)) # <class 'list'>
# type 返回元素类型
print(type(tuple_name)) # <class 'tuple'>
# del 删除整个元组对象
tuple_del = ('ok', 'hello', 'world', 'java')
print(tuple_del) # ('ok', 'hello', 'world', 'java')
del(tuple_del)
print(tuple_del) # NameError: name 'tuple_del' is not defined
# sum 元组中所有元素进行求和
tuple_sum = (123, 456, 999)
print(sum(tuple_sum)) # 1578