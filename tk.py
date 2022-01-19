import tkinter as tk
from tkinter import *
from tkinter import messagebox

win = tk.Tk()
win.geometry("500x500")
win.title("練習tkinter")
label = tk.Label(win, text="試試標籤")
label.pack()

but1 = tk.Button(win, width=30, text="試試按紐")
but1.pack()
but2 = tk.Button(win, width=30, text="試試按紐2")
but2.pack()

entry = tk.Entry(win, width=30, bg='yellow', fg='black', show='*')
entry.pack()

sentences="這是一個特殊的模板，用來實驗文字方塊，\n 話說，快傍晚了，想想晚餐吃什麼吧"
text = tk.Text(win, width=50, height=5, bg='pink', wrap=WORD)
text.insert(END, sentences)
text.pack()

def show_msg():
    # messagebox.showinfo('顯示類對話方塊', '顯示內容在此')  # icon=藍色i
    # messagebox.showerror('顯示類對話方塊', '顯示內容在此')  # icon=叉叉
    messagebox.showwarning('顯示類對話方塊', '顯示內容在此')  # icon=三角驚嘆號
def inter_msg():
    # messagebox.askretrycancel('詢問互動類對話方塊', '詢問對話方塊內容在此') # icon=三角驚嘆號
    # messagebox.askokcancel('詢問互動類對話方塊', '詢問對話方塊內容在此')  # icon=藍色問號
    # messagebox.askyesno('詢問互動類對話方塊', '詢問對話方塊內容在此')  # icon=藍色問號
    # messagebox.askquestion('詢問互動類對話方塊', '詢問對話方塊內容在此')  # icon=藍色問號
    messagebox.askyesnocancel('詢問互動類對話方塊', '詢問對話方塊內容在此')  # icon=藍色問號, 三個選項


b1 = Button(win, width=30, text='顯示類對話方塊', command=show_msg)
b1.pack()
b2 = Button(win, width=30, text='詢問互動類對話方塊', command=inter_msg).pack()


def check():
    print('點選內容有: ', var1.get(), var2.get(), var3.get())
    import main


lb1 = Label(win, text='選項: ')
item1 = '選項1'
item2 = '選項2'
item3 = '選項3'
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
chk1 = Checkbutton(win, text=item1, variable=var1, onvalue=item1, offvalue='')
chk2 = Checkbutton(win, text=item2, variable=var2, onvalue=item2, offvalue='')
chk3 = Checkbutton(win, text=item3, variable=var3, onvalue=item3, offvalue='')
chk1.pack()
chk2.pack()
chk3.pack()
btnShow = Button(win, text='列出選擇結果', command=check)
btnShow.pack()

win.mainloop()