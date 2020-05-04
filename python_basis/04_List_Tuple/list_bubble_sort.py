# 冒泡排序
def bubble_sort(num):
    length = len(num)
    for i in range(length):
        for j in range(0, length - i-1):
            if num[j] > num[j+1]:
                num[j], num[j + 1] = num[j + 1], num[j]

num = [1, 34, 5, 76, 999, 787]
bubble_sort(num)
print(num)
for i in range(len(num)):
    print ("%d" %num[i]),
