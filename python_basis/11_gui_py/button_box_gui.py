from tkinter import tix
import tkinter


def btnDialog(w):
    btn_box = tix.ButtonBox(w, orientation=tix.HORIZONTAL)
    btn_box.add('hello', text='确认', underline=0,
                width=5, command=lambda w=w: w.destroy())
    btn_box.add('close', text='取消', underline=0,
                width=5, command=lambda w=w: w.destroy())
    btn_box.pack(side=tix.BOTTOM, fill=tix.X)

if __name__ == '__main__':
    root = tix.Tk()
    btnDialog(root)
    root.mainloop()
