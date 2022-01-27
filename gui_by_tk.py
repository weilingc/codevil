import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

# 做一個遊戲視窗
game_win = tk.Tk()
game_win.geometry("700x500")
game_win.title("Codevil")

hero_role = ['Darevil', 'Elek']
bad_role = ['Bad_cop','Corp_cop','Kingpin']


Label(game_win, text="請問您要選擇的英雄人物有: ", justify=LEFT, padx=20).pack()
var_list = []
for i in hero_role:
    # print(var1)
    index = str(hero_role.index(i)+1)
    globals()['var'+index] = StringVar()
    var_list.append(globals()['var'+index])
    globals()['chk'+index] = Checkbutton(game_win, text=i, variable=globals()['var'+index], onvalue=i, offvalue='')
    globals()['chk'+index].pack()

Label(game_win, text="請問您要選擇的反派人物有: ", justify=RIGHT, padx=20).pack()
b_var_list = []
for j in bad_role:
    index = str(bad_role.index(j)+1)
    globals()['b_var'+index] = StringVar()
    b_var_list.append(globals()['b_var'+index])
    globals()['b_chk'+index] = Checkbutton(game_win, text=j, variable=globals()['b_var'+index], onvalue=j, offvalue='')
    globals()['b_chk'+index].pack()

def check():
    the_str = ''
    for i in var_list+b_var_list:
        if i.get() != '':
            the_str += str(i.get()) + '\n'
    messagebox.showinfo('人物選擇結果 ', the_str)


btnShow = Button(game_win, text='人物選擇結果', command=check)
btnShow.pack()

# text = tk.Text(game_win, width=50, height=5, bg='pink', wrap=WORD)
# text.insert(END, sentences)
# text.pack()






def show_msg():
    pass


mainloop()