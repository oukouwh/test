# 使用Threading类方式实现买票
import threading
from time import *
from datetime import datetime
tickets = [
    ['2020/05/05', '上海', '北京', 10, 145],
    ['2020/05/05', '青岛', '济南', 4, 64],
    ['2020/05/05', '厦门', '杭州', 12, 198],
    ['2020/05/05', '武汉', '长沙', 0, 80]
]


def buy_tickets(name, nums, date1, station):
    i = 0
    sleep(1)
    for recode in tickets:
        if recode[0] == date1 and recode[1] == station:
            if recode[3] >= nums:
                tickets[i][3] = recode[3]-nums
                print('%s购买%d张票成功' % (name, nums))
                return
            else:
                print('%s车票数量不足无法购买' % (name))
                return -1
        i += 1
    print('今日票已经售完，无法购买')
    return -1


class my_thread(threading.Thread):
    def __init__(self, target, args):
        threading.Thread.__init__(self)
        self.target = target
        self.args = args

    def run(self):
        self.target(*self.args)


if __name__ == '__main__':
    user_info = [
        ('Jack', 7, '2020/05/05', '上海'),
        ('Alex', 3, '2020/05/05', '上海'),
        ('切格瓦拉', 2, '2020/05/05', '武汉')
    ]
    list_data = []
    print('Start:', datetime.now())
    for info in user_info:
        get_info = my_thread(target=buy_tickets, args=info)
        list_data.append(get_info)
    for i in range(len(list_data)):
        list_data[i].start()
    for i in range(len(list_data)):
        list_data[i].join()

    print('END:', datetime.now())
    print('剩余票数为:\n')
    for i in tickets:
        print(i)

# Start: 2020-05-05 11:11:06.216749
# 切格瓦拉车票数量不足无法购买Jack购买7张票成功
# Alex购买3张票成功
# END: 2020-05-05 11:11:07.219607
# 剩余票数为:
# ['2020/05/05', '上海', '北京', 0, 145]
# ['2020/05/05', '青岛', '济南', 4, 64]
# ['2020/05/05', '厦门', '杭州', 12, 198]
# ['2020/05/05', '武汉', '长沙', 0, 80]