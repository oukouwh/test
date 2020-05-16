day = int(input('请输入天数:'))
hour = int(input('请输入小时:'))
minute = int(input('请输入分钟:'))
result = day * 60 *24 * 60 + hour *60 * 60 + minute*60
print(result)