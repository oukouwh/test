# tkinter开发工具包
import tkinter 
MainForm = tkinter.Tk()
MainForm.title('GUI界面') # # 设置标题属性
MainForm.geometry('300x300')
# 设置窗体背景色
MainForm['background'] = 'LightSlateGray'
# 向窗体上添加组件
btn = tkinter.Button(MainForm,text = '退出',fg = 'red')
btn1 = tkinter.Button(MainForm,text = '加入',fg = 'black')
btn2 = tkinter.Button(MainForm,text = '返回',fg = 'green')
btn.pack(side='left',padx='1m')
btn1.pack(side='left',padx='1m')
btn2.pack(side='left',padx='1m')
# btn.pack(side='top')
# btn1.pack(side='top')
# btn2.pack(side='top')
MainForm.mainloop()


