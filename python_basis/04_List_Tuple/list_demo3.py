list_one = ['A','B','C','D']
list_two = ['a','b','c','d']
list_sum = []
for i in list_one:
    for j in list_two:
        list_sum.append(i+j)
print(list_sum)
# ['Aa', 'Ab', 'Ac', 'Ad', 'Ba', 'Bb', 'Bc', 'Bd', 'Ca', 'Cb', 'Cc', 'Cd', 'Da', 'Db', 'Dc', 'Dd']
list_sum1 = [i+j for i in list_one  for j in list_two] # 列表推导式
print(list_sum1)
# ['Aa', 'Ab', 'Ac', 'Ad', 'Ba', 'Bb', 'Bc', 'Bd', 'Ca', 'Cb', 'Cc', 'Cd', 'Da', 'Db', 'Dc', 'Dd']