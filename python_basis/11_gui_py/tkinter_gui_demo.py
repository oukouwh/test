from tkinter import *
# menu案例
root = Tk()
menu_gui = Menu(root)
root.config(menu=menu_gui)
def callback():
    root.title('hello')
filemenu = Menu(menu_gui)
menu_gui.add_cascade(label='File',menu=filemenu) # 建立子菜单实例
menu_gui.add_cascade(label='Edit',menu=filemenu) # 建立子菜单实例
menu_gui.add_cascade(label='View',menu=filemenu) # 建立子菜单实例
filemenu.add_command(label='New',command=callback) # 设置子菜单
filemenu.add_command(label='Open',command=callback) # 设置子菜单
filemenu.add_separator() # 增加分割线
filemenu.add_command(label='Exit',command=callback)  # 设置子菜单
mainloop()
