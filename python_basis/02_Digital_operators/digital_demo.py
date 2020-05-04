# 测试小案例
num1, num2, num3 = 5, 6, 9
price1, price2, price3 = 2.3, 4.7, 3.8
order1, order2, order3 = '啤酒', '饮料', '矿泉水'
date = '2020年04月24日'
sum_num = num1 + num2 + num3  # 总数量
sum_price = num1*price1 + num2 * price2+num3*price3  # 总金额
print('----------消费账单-------------')
print('消费地点     ' +'消费时间     ' + '消费数量     ' + '消费金额    ' + '订单名称')
print('万达广场     ' +date           +  str(num1)    +''+str(price1)    + order1)
print('万达广场     ' +date           +  str(num2)     +''+str(price2)    + order2)
print('万达广场     ' +date           +  str(num3)      +''+str(price3)    + order3)
print('消费总金额；%.2f' %(sum_price) + '消费总数量%d:' %(sum_num))