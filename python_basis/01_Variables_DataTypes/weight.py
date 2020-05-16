int_weight = float(input('请输入重量:'))
result_kg = int_weight // 16
result_g = int_weight % 16
print('重量为%d斤%d两'%(result_kg,result_g))