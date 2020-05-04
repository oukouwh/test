# JSON格式文件
# json常用的两种数据结构类型是键值对和有序列表
# python自带处理json数据类型的json模块
import json
json_tuple = {'1':'A', '2':'B', '3':'C'} # 定义字典
print(json_tuple) # {'1': 'A', '2': 'B', '3': 'C'}
tuple_to_json = json.dumps(json_tuple) # 字典转json
print(tuple_to_json) # {"1": "A", "2": "B", "3": "C"}
json_to_python = json.loads(tuple_to_json)
print(json_to_python) # {'1': 'A', '2': 'B', '3': 'C'}