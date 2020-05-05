from time import *
from datetime import datetime
# 无线程车票购买案例
tickets=[
        ['2020/05/05','上海','北京',10,145],
        ['2020/05/05','青岛','济南',4,64],
        ['2020/05/05','厦门','杭州',12,198],
        ['2020/05/05','武汉','长沙',0,80]
]

def buy_tickets(name,nums,date1,station):
    i=0
    sleep(1)
    for recode in tickets:
        if recode[0] == date1 and recode[1] == station:
            if recode[3]>= nums:
                tickets[i][3]=recode[3]-nums
                return nums
            else:
                print('数量不足无法购买')
                return -1
        i+=1
    print('今日票已经售完，无法购买')
    return -1

if __name__ =='__main__':
    print('Start:',datetime.now())
    result = buy_tickets('Jack',7,'2020/05/05','上海')
    if result>0:
        print('Jcak购买%d张票成功'%(7))
    result = buy_tickets('Alex',3,'2020/05/05','上海')
    if result>0:
        print('Alex购买%d张票成功'%(3))
    result = buy_tickets('切格瓦拉',2,'2020/05/05','武汉')
    if result>0:
        print('切格瓦拉购买%d张票成功'%(2))
    print('END:',datetime.now())
    print('剩余票数为:\n')
    for i in tickets:
        print(i)

# Start: 2020-05-05 09:37:54.422077
# Jcak购买7张票成功
# Alex购买3张票成功
# 数量不足无法购买
# END: 2020-05-05 09:37:57.423694
# 剩余票数为:
# ['2020/05/05', '上海', '北京', 0, 145]
# ['2020/05/05', '青岛', '济南', 4, 64]
# ['2020/05/05', '厦门', '杭州', 12, 198]
# ['2020/05/05', '武汉', '长沙', 0, 80]