#  _*_ coding:   utf-8 _*_
import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

from config import bg, bt_font, bt_bg, child_size


class Change(tk.Tk):
    id=None
    def __init__(self):
        self.db = sqlite3.connect('static/data.db')
        self.cursor = self.db.cursor()
        super(Change, self).__init__()
        self.configure(bg=bg)
        self.title("书籍信息修改")
        self.geometry(child_size)
        title = tk.Label(self,text='书名:',bg=bg,font=bt_font)
        title.grid(row=1,column=1,padx=30,pady=20)
        author = tk.Label(self, text='作者:', bg=bg,
                         font=bt_font)
        author.grid(row=2, column=1)
        press = tk.Label(self, text='出版社:', bg=bg,
                         font=bt_font)
        press.grid(row=3, column=1,pady=20)

        category= tk.Label(self, text='类别:', bg=bg,
                         font=bt_font)
        category.grid(row=4, column=1)

        self.booktitle = ttk.Entry(self)
        self.bookauthor = ttk.Entry(self)
        self.bookpress = ttk.Entry(self)


        self.booktitle.grid(row=1,column=2)
        self.bookauthor.grid(row=2,column=2)
        self.bookpress.grid(row=3,column=2)

        self.sub = tk.Button(self,text='提交修改',font=bt_font,bg=bt_bg,command=self.commit)
        self.sub.grid(row=5,column=2,pady=10)
        # 设置条件下拉框
        self.category_choice = tk.StringVar()
        self.category_conditon = ttk.Combobox(self,
                                            width=10,
                                            textvariable=
                                            self.category_choice)
        self.category_conditon['values'] = ('小说','专业书','工具书','报告','其他')
        self.category_conditon.grid(row=4,column=2, sticky=tk.W)

    def commit(self):
        title = self.booktitle.get()
        author = self.bookauthor.get()
        press = self.bookpress.get()
        category = self.category_conditon.get()
        print(self.id,title,author,press,category)
        if title=='' or author=='' or press=='' or category=='':
            tkinter.messagebox.showinfo('提示', '信息不能为空!')
            self.destroy()
            return None
        self.cursor.execute(f'update books set title="{title}",author="{author}",press="{press}",category="{category}" where id="{self.id}"')
        self.db.commit()
        tkinter.messagebox.showinfo('提示','书籍信息修改成功!')
        self.destroy()




    def __del__(self):
        self.db.close()


if __name__=='__main__':
    Change().mainloop()