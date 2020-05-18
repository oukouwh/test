list_number = [23,45,2,13,65,77]
# 取数据
for item in range(len(list_number) -1):
    # 作比较
    for i in range(item+1,len(list_number)):
        if list_number[item] > list_number[i]:
            list_number[item],list_number[i] = list_number[i],list_number[item]
print(list_number)