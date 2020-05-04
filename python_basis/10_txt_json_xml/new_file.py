# 新建文本文件 C:\py_vscod
file_path = 'c:\\py_vscod\\test.txt'  # 定义文件名和路径
new_file = open(file_path, 'w')
new_file.close()
print('%s创建成功' % (new_file))
# <_io.TextIOWrapper name='c:\\py_vscod\\test.txt' mode='w' encoding='cp936'>创建成功
# 基本的读写文件
file_path = 'c:\\py_vscod\\test.txt'
new_file = open(file_path, 'w')
file_write = new_file.write('hello python')
print('写入的内容%d字节' % (file_write))
# 写入的内容12字节
# 用文件对象read()读取内容
new_file = open(file_path, 'r')
file_read = new_file.read()
print('读取的内容%s' % (file_read))  # 读取的内容hello python
new_file.close()

# 复杂的读写文件
# 一次性写入多行文件
nums = ['1', '2', '3', '4', '5', '6']
file_path = 'c:\\py_vscod\\test.txt'
new_file = open(file_path, 'a')
for i in nums:
    new_file.write(i+'\n')
new_file.close()
print('写入多行结束')

# 一次性读取多行文件
# file_path = r'c:\py_vscod\test.txt'
new_file = open(r'c:\py_vscod\test.txt', 'r')
read_line = 1
while read_line:
    read_line = new_file.readline()
    print(read_line)
    # hello python1
# 2
# 3
# 4
# 5
# 6

# 以列表格式读取多行
new_file = open(r'c:\py_vscod\test.txt', 'r')
read_line = new_file.readlines()
print(read_line)
# ['hello python1\n', '2\n', '3\n', '4\n', '5\n', '6\n']

# 连续读取特定字节数量的内容
new_file = open(r'c:\py_vscod\test.txt', 'r')
read_line = new_file.readline(2) # he 读取开头两个字节
print(read_line) 
print(new_file.readline()) # llo python1 读取剩余字节

# 在指定文职读取内容
# file.tell() 返回当前文件可以读写的位置字节数
new_file = open(r'c:\py_vscod\test.txt', 'r')
read_line = new_file.readline() 
print(read_line)  # hello python1
file_tell = new_file.tell() # he 读取开头两个字节
print(file_tell)  # 15

# 在指定位置写内容
# file.seek
new_file = open(r'c:\py_vscod\test.txt', 'w')
# read_line = new_file.readline() 
# print(read_line) 
new_file.seek(16) 
new_file.write('hahaha')
new_file.close()
print(new_file)   # <_io.TextIOWrapper name='c:\\py_vscod\\test.txt' mode='w' encoding='cp936'>


# 文件异常处理
file_path = r'c:\py_vscod\test1.txt'
flag = False
try:
    file_op = open(file_path,'r')
    print(file_op.read())
    flag = True
except:
    print('打开文件%s出错，请检查'%(file_path))
finally:
    if flag:
        file_op.close()
        print('文件关闭')
    else:
        print('程序退出')

# 打开文件c:\py_vscod\test1.txt出错，请检查
# 程序退出