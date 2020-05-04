# 递归算法
def recs_sum(num):
    if num == 1:
        return num
    return recs_sum(num - 1) * num
print(recs_sum(6))