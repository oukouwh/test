from time import *
from datetime import datetime
import threading
# threading函数实现车票购买案例
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
                print('%s购买%d张票成功'%(name,nums))
                return
            else:
                print('%s车票数量不足无法购买'%(name))
                return -1
        i+=1
    print('今日票已经售完，无法购买')
    return -1

if __name__ =='__main__':
    print('Start:',datetime.now())
    t1 = threading.Thread(target=buy_tickets,args=('Jack',7,'2020/05/05','上海'))
    t2 = threading.Thread(target=buy_tickets,args=('Alex',3,'2020/05/05','上海'))
    t3 = threading.Thread(target=buy_tickets,args=('切格瓦拉',2,'2020/05/05','武汉'))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('END:',datetime.now())
    print('剩余票数为:\n')
    for i in tickets:
        print(i)

# Start: 2020-05-05 09:48:08.167276
# 切格瓦拉车票数量不足无法购买Alex购买3张票成功Jack购买7张票成功
# END: 2020-05-05 09:48:09.168338
# 剩余票数为:
# ['2020/05/05', '上海', '北京', 0, 145]
# ['2020/05/05', '青岛', '济南', 4, 64]
# ['2020/05/05', '厦门', '杭州', 12, 198]
# ['2020/05/05', '武汉', '长沙', 0, 80]