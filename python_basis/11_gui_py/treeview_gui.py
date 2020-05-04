from tkinter import *
from tkinter import ttk
# 树状结构列表
root = Tk()
root.title('数据树状结构图')
tree = ttk.Treeview(root)
tree['columns'] = ('one','two') # 设置两个对象列名
# 设置第一个列宽和第二个列宽
tree.column('one',widt=100)
tree.column('two',widt=100)
# 设置列的标题名
tree.heading('one',text='姓名')
tree.heading('two',text='年龄')
# 在第一行插入数据
tree.insert('',0,text='班主任',values=('王老师',25))
id1 = tree.insert('',1,text='班委')
tree.insert(id1,'end',text='班长',values=('小王',20))
tree.insert(id1,'end',text='体育委员',values=('小丽',20))
id2 = tree.insert('',2,text='团员')
tree.insert(id2,'end',text='男生',values=('小李',20))
tree.insert(id2,'end',text='女生',values=('小丽',20))
tree.pack()
root.mainloop()