

import tkinter as tk
from tkinter import ttk
from config import bg, child_size,bt_bg,bt_font
from model import db, cursor


class StaticMain(tk.Tk):
    def __init__(self):
        super(StaticMain, self).__init__()
        self.configure(bg=bg)
        self.title("请选择统计方式")
        self.geometry(child_size)
        self.button1 = tk.Button(self,text='类别',bg= bt_bg,width=15,height=2,command=self.show_category)
        self.button2 = tk.Button(self,text='书名',bg= bt_bg,width=15,height=2,command=self.show_title)
        self.button3 = tk.Button(self,text='作者',bg= bt_bg,width=15,height=2,command=self.show_author)
        self.button4 = tk.Button(self,text='出版社',bg= bt_bg,width=15,height=2,command=self.show_press)
        self.button1.grid(row=1,column=1,padx=20,pady=40)
        self.button2.grid(row=1, column=2)
        self.button3.grid(row=2, column=1)
        self.button4.grid(row=2, column=2)
    def show_category(self):
        self.destroy()
        Category()
    def show_title(self):
        self.destroy()
        Title()
    def show_author(self):
        self.destroy()
        Author()
    def show_press(self):
        self.destroy()
        Press()

# 类别统计
class Category(tk.Tk):
    def __init__(self):
        self.db = db
        self.cursor = cursor
        self.count = 0
        super(Category, self).__init__()
        self.geometry('750x500+300+100')
        self.title('类别统计')
        self.configure(bg=bg)
        self.label = tk.Label(self,text='请选择类别:',bg=bg,font=bt_font)
        self.label.place(relx=0.1,rely=0.025)
        # 设置条件下拉框
        self.search_conditon_choice = tk.StringVar()
        self.search_conditon = ttk.Combobox(self,
                                            width=10,
                                            textvariable=
                                            self.search_conditon_choice)
        self.search_conditon['values'] = ('小说','其他','专业书','报告','工具书')
        self.search_conditon.place(relx=0.25,rely=0.03)

        self.button = tk.Button(self,text='开始统计',font=bt_font,bg=bt_bg,command=self.search)
        self.button.place(relx=0.4,rely=0.02)
        self.label2 = tk.Label(self,text='',bg=bg,fg='red',font=bt_font)
        self.label2.place(relx=0.55,rely=0.024)

        self.text = tk.Text(self,width=73,height=20,font=bt_font)
        self.text.place(relx=0.1,rely=0.15)
        self.mainloop()
    def search(self):
        self.text.delete('1.0',tk.END)
        key = self.search_conditon.get()
        data = self.cursor.execute(f'select * from books where category="{key}"').fetchall()
        if data==[]:
            return None
        self.text.insert(tk.END,'书名'+'\t\t'+'作者'+'\t\t'+'出版社'+'\t\t'+'类别')
        self.count=len(data)
        for i in data:
            self.text.insert(tk.END,'\n')
            self.text.insert(tk.END,'\t\t'.join(i[1:]))
        self.label2.configure(text=f'该类别书籍数量为:  {self.count}')
    def __del__(self):
        self.db.close()

# 书名统计
class Title(tk.Tk):
    def __init__(self):
        self.db = db
        self.cursor = cursor
        self.count = 0
        super(Title, self).__init__()
        self.geometry('750x500+300+100')
        self.title('书名统计')
        self.configure(bg=bg)
        self.label = tk.Label(self,text='请输入书名:',bg=bg,font=bt_font)
        self.label.place(relx=0.1,rely=0.05)
        self.e = ttk.Entry(self)
        self.e.place(relx=0.2,rely=0.05)
        self.btn = tk.Button(self,text='开始统计',font=bt_font,bg=bt_bg,command=self.sub)
        self.btn.place(relx=0.45,rely=0.042)
        self.label2 = tk.Label(self, text='', bg=bg,
                               fg='red', font=bt_font)
        self.label2.place(relx=0.65, rely=0.042)
        # 设置文本框
        self.text = tk.Text(self, width=73, height=20,
                            font=bt_font)
        self.text.place(relx=0.1, rely=0.15)
        self.mainloop()
    def __del__(self):
        self.db.close()
    def sub(self):
        value = self.e.get()
        if value:
            sql = f'select * from books where title="{value}"'
            data = self.cursor.execute(sql).fetchall()
            self.count=len(data)
            if data:
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.END, '序号' + '\t\t' +
                                 '书名' + '\t\t' + '作者' +
                                 '\t\t' + '出版社' + '\t\t' + '类别')
                for i in data:
                    i = [str(j) for j in i]
                    self.text.insert(tk.END, '\n')
                    self.text.insert(tk.END, '\t\t'.join(i))
                self.label2.configure(
                    text=f'该书名的书籍数量为:  {self.count}')



# 作者统计
class Author(tk.Tk):
    def __init__(self):
        self.db = db
        self.cursor = cursor
        self.count = 0
        super(Author, self).__init__()
        self.geometry('750x500+300+100')
        self.title('作者统计')
        self.configure(bg=bg)
        self.label = tk.Label(self, text='请输入作者:', bg=bg,
                              font=bt_font)
        self.label.place(relx=0.1, rely=0.05)
        self.e = ttk.Entry(self)
        self.e.place(relx=0.2, rely=0.05)
        self.btn = tk.Button(self, text='开始统计',
                             font=bt_font, bg=bt_bg,
                             command=self.sub)
        self.btn.place(relx=0.45, rely=0.042)
        self.label2 = tk.Label(self, text='', bg=bg,
                               fg='red', font=bt_font)
        self.label2.place(relx=0.65, rely=0.042)
        # 设置文本框
        self.text = tk.Text(self, width=73, height=20,
                            font=bt_font)
        self.text.place(relx=0.1, rely=0.15)
        self.mainloop()

    def __del__(self):
        self.db.close()
    def sub(self):
        value = self.e.get()
        if value:
            sql = f'select * from books where author="{value}"'
            data = self.cursor.execute(sql).fetchall()
            self.count=len(data)
            if data:
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.END, '序号' + '\t\t' +
                                 '书名' + '\t\t' + '作者' +
                                 '\t\t' + '出版社' + '\t\t' + '类别')
                for i in data:
                    i = [str(j) for j in i]
                    self.text.insert(tk.END, '\n')
                    self.text.insert(tk.END, '\t\t'.join(i))
                self.label2.configure(
                    text=f'该作者的书籍数量为:  {self.count}')


# 出版社统计
class Press(tk.Tk):
    def __init__(self):
        self.db = db
        self.cursor = cursor
        self.count = 0
        super(Press, self).__init__()
        self.geometry('750x500+300+100')
        self.title('出版社统计')
        self.configure(bg=bg)
        self.label = tk.Label(self, text='请输入出版社:', bg=bg,
                              font=bt_font)
        self.label.place(relx=0.1, rely=0.05)
        self.e = ttk.Entry(self)
        self.e.place(relx=0.2, rely=0.05)
        self.btn = tk.Button(self, text='开始统计',
                             font=bt_font, bg=bt_bg,
                             command=self.sub)
        self.btn.place(relx=0.45, rely=0.042)
        self.label2 = tk.Label(self, text='', bg=bg,
                               fg='red', font=bt_font)
        self.label2.place(relx=0.65, rely=0.042)
        # 设置文本框
        self.text = tk.Text(self, width=73, height=20,
                            font=bt_font)
        self.text.place(relx=0.1, rely=0.15)
        self.mainloop()

    def __del__(self):
        self.db.close()

    def sub(self):
        value = self.e.get()
        if value:
            sql = f'select * from books where press="' \
                  f'{value}"'
            data = self.cursor.execute(sql).fetchall()
            self.count = len(data)
            if data:
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.END, '序号' + '\t\t' +
                                 '书名' + '\t\t' + '作者' +
                                 '\t\t' + '出版社' + '\t\t'
                                 + '类别')
                for i in data:
                    i = [str(j) for j in i]
                    self.text.insert(tk.END, '\n')
                    self.text.insert(tk.END, '\t\t'.join(i))
                self.label2.configure(
                    text=f'该出版社的书籍数量为:  {self.count}')


if __name__=='__main__':
    StaticMain().mainloop()