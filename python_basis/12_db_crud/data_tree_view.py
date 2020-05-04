def fun_click(event):
    get_sql_data()


def get_sql_data():
    import pymysql  # 导入数据库驱动程序模块
    import sys  # 导入sys模块
    try:
        conn = pymysql.connect(host='localhost', user='root',
                            password='123456A', db='py_database', port=3306, charset='utf8')
    except:
        print('数据库连接出现错误，请重试')
        conn.close()
        sys.exit()
# ===============================数据库的CRUD操作
    cur = conn.cursor()  # 创建游标实例
    # 查询数据
    select_sql = "select * from userinfo"
    cur.execute(select_sql)
    list_data = []
    for i in cur.fetchall():
        tree.insert('',0,values=(i[0],i[1]))
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('数据库查询数据可视化界面')
tree = ttk.Treeview(root)
tree['columns'] = ('username','password')
tree.column('username', width=50)
tree.heading('username', text='用户名')
tree.column('password', width=50)
tree.heading('password', text='密码')
tree.pack(side='top')
btn = tk.Button(root, text='查询数据', width=15)
btn.bind('<Button-1>', fun_click)
btn.pack(side='top')
root.mainloop()
