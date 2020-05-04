from datetime import datetime, date, time
# datetime时间模块
# datetime包括date，time的所有功能 以下为datetime的实例方法
# datetime.now() 获取当前日期和时间
now = datetime.now()  # 获取当前datetime
print(now)  # 2020-04-30 15:46:34.516139
# datetime.date(t) 获取当天的日期，t为datetime的实例参数
print(datetime.date(now))  # 2020-04-30
# datetime.time(t) 获取当天的时间，t为datetime的实例参数
print(datetime.time(now))  # 15:48:22.613439
# datetime.ctime(t) 获取星期月日时分秒年格式的字符串，t为datetime的实例参数
print(datetime.ctime(now))  # Thu Apr 30 15:48:38 2020
# datetime.utcnow() 获取当前的UTC日期和时间
print(datetime.utcnow())
# datetime.timestamp(t) 获取当天的时间戳(UNIX时间戳)，t为datetime的实例参数
print(datetime.timestamp(now))  # 1588229564.917201
# datetime.fromtimestamp(t_tamp) 根据时间戳返回UTC日期时间，t_tamp为时间戳浮点数
# 2020-04-30 15:54:57.402943
print(datetime.fromtimestamp(datetime.timestamp(now)))
# datetime.combine(date,time) 绑定日期时间，生成新的datetime对象date对象为日期对象，time为时间对象
date1 = date(2020, 11, 11)
time1 = time(11, 11, 11)
print(datetime.combine(date1, time1))  # 2020-11-11 11:11:11
# datetime.strptime(dt_str,sf) 根据字符串和指定格式生成新的datetime对象，dt_str为字符串日期对象，sf为指定的格式
newDate = datetime.strptime("12/12/20 09:40", '%d/%m/%y %H:%M')
print(newDate)  # 2020-12-12 09:40:00
# datetime.timetuple(t) 把datetime对象所有属性转为时间元组对象，t为datetime的实例参数
print(datetime.timetuple(now))
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=30, tm_hour=16, tm_min=15, tm_sec=43, tm_wday=3, tm_yday=121, tm_isdst=-1)
# datetime.isocalendar() 获取iso格式的日期(元组形式)
print(now.isocalendar())  # (2020, 18, 4)
# datetime.strftime(dt_str_format) 获取自定义格式的日期时间字符串，dt_str_format指定格式
print(now.strftime('%Y-%m-%d %H:%M:%S %p')) # 2020-04-30 16:24:58 PM
# 遇到的问题
# 当时是把这个.py的文件名写成了datetime.py，导致出现了一下的错误,更改一下文件名就可以了
# ImportError: cannot import name 'datetime' from 'datetime'
