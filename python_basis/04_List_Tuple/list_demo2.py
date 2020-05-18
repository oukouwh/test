list_number = [10,10,30,40,50,30]
dict_number = {}
# 取数据

for item in list_number:
   if list_number.count(item) > 1:
       dict_number[item] = list_number.count(item)

print(dict_number)