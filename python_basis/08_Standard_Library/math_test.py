# math模块提供很多数学计算函数
import math
# 浮点取整trunc(x) x为浮点数
print(math.trunc(3.5)) # 3
# math.ceil(x) 取整向上取整 取大于x的最小整数
print(math.ceil(9.06)) # 10 
# round(x) 四舍五入 
print(round(3.4)) # 3
print(round(3.5)) # 4
# 对元组的元素求和返回浮点数
t_num = (1,3,4,6)
print(math.fsum(t_num)) # 14.0
# 对列表的元素求和返回浮点数
l_num = [1,3,4,3]
print(math.fsum(l_num)) # 11.0
print(sum(l_num)) # 11
l_num_f = [1,3.9,4,3]
print(sum(l_num_f)) # 11.9
