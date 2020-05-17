day = int(input('请输入天数:'))
hour = int(input('请输入小时:'))
minute = int(input('请输入分钟:'))
result = day * 60 *24 * 60 + hour *60 * 60 + minute*60
print(result)

str_message = '上海自来水来自海上'
if str_message == str_message[::-1]:
    print('是回文')
else:
    print('不是回文')

