

import tkinter as tk
from tkinter import ttk
from config import bg, bt_bg, child_size, bt_font
from model import cursor, db
from tkinter.messagebox import showinfo


class Sort(tk.Tk):
    def __init__(self):
        super(Sort, self).__init__()
        self.configure(bg=bg)
        self.title("请选择排序方式")
        self.geometry(child_size)
        self.button1 = tk.Button(self, text='单一字段排序', bg=bt_bg,command=self.odd,
                                 width=15, height=2,)
        self.button2 = tk.Button(self, text='组合字段排序', bg=bt_bg,command=self.pair,
                                 width=15, height=2)
        self.button1.grid(row=1, column=1, padx=90, pady=40)
        self.button2.grid(row=2, column=1)
    def odd(self):
        self.destroy()
        Odd()
    def pair(self):
        self.destroy()
        Pair()


# 单一字段排序
class Odd(tk.Tk):
    def __init__(self):
        self.db = db
        self.cursor = cursor
        super(Odd, self).__init__()
        self.configure(bg=bg)
        self.title('单一字段排序')
        self.geometry('750x500+300+100')
        self.label = tk.Label(self,text='请选择字段:',font=bt_font,bg=bg)
        self.label.place(relx=0.1,rely=0.05)
        # 设置条件下拉框
        self.search_conditon_choice = tk.StringVar()
        self.search_conditon = ttk.Combobox(self,
                                            width=10,
                                            textvariable=
                                            self.search_conditon_choice)
        self.search_conditon['values'] =  ('序号','书名','作者','出版社','类别')
        self.search_conditon.place(relx=0.22,rely=0.05)
        self.label2 = tk.Label(self,text='请选择排序方式:',font=bt_font,bg=bg)
        self.label2.place(relx=0.4,rely=0.05)

        # 设置排序方式下拉框
        self.search_conditon_choice2 = tk.StringVar()
        self.search_conditon2 = ttk.Combobox(self,
                                            width=10,
                                            textvariable=
                                            self.search_conditon_choice2)
        self.search_conditon2['values'] = ('降序','升序')
        self.search_conditon2.place(relx=0.55, rely=0.05)

        self.btn = tk.Button(self,text='开始排序',bg=bt_bg,font=bt_font,command=self.sub)
        self.btn.place(relx=0.75,rely=0.04)
        # 设置文本框
        self.text = tk.Text(self, width=73, height=20,
                            font=bt_font)
        self.text.place(relx=0.1, rely=0.15)

        self.mainloop()
    def sub(self):
        key = self.search_conditon.get()
        value = self.search_conditon2.get()
        if key and value:
            dic = {'序号':'id','书名': 'title', '作者': 'author',
                   '出版社': 'press', '类别': 'category'}
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END,'序号'+'\t\t'+
                             '书名' + '\t\t' + '作者' + '\t\t' + '出版社' + '\t\t' + '类别')
            if value=='升序':
                sql = f'select * from books order by "{dic.get(key)}"'
                data = self.cursor.execute(sql).fetchall()
            else:
                sql = f'select * from books order by "{dic.get(key)}" desc'
                data = self.cursor.execute(sql).fetchall()
            for i in data:
                i=[str(j) for j in i]
                self.text.insert(tk.END, '\n')
                self.text.insert(tk.END, '\t\t'.join(i))

    def __del__(self):
        self.db.close()

# 组合字段排序
class Pair(tk.Tk):
    def __init__(self):
        super(Pair, self).__init__()
        self.db = db
        self.cursor = cursor
        self.configure(bg=bg)
        self.title('组合字段排序')
        self.geometry('750x500+300+100')
        # 一级字段
        self.label = tk.Label(self, text='一级字段:',
                              font=bt_font, bg=bg)
        self.label.place(relx=0.1, rely=0.05)
        self.search_conditon_choice = tk.StringVar()
        self.search_conditon = ttk.Combobox(self,
                                            width=10,
                                            textvariable=
                                            self.search_conditon_choice)
        self.search_conditon['values'] = (
        '序号', '书名', '作者', '出版社', '类别')
        self.search_conditon.place(relx=0.22, rely=0.05)
        self.label2 = tk.Label(self, text='请选择排序方式:',
                               font=bt_font, bg=bg)
        self.label2.place(relx=0.4, rely=0.05)
        self.search_conditon_choice2 = tk.StringVar()
        self.search_conditon2 = ttk.Combobox(self,
                                             width=10,
                                             textvariable=
                                             self.search_conditon_choice2)
        self.search_conditon2['values'] = ('降序', '升序')
        self.search_conditon2.place(relx=0.55, rely=0.05)
        # 二级字段
        self.label2 = tk.Label(self, text='次级字段:',
                              font=bt_font, bg=bg)
        self.label2.place(relx=0.1, rely=0.15)
        self.search_conditon_choice3 = tk.StringVar()
        self.search_conditon3 = ttk.Combobox(self,
                                            width=10,
                                            textvariable=
                                            self.search_conditon_choice3)
        self.search_conditon3['values'] = (
            '序号', '书名', '作者', '出版社', '类别')
        self.search_conditon3.place(relx=0.22, rely=0.15)
        self.label22 = tk.Label(self, text='请选择排序方式:',
                               font=bt_font, bg=bg)
        self.label22.place(relx=0.4, rely=0.15)
        self.search_conditon_choice4 = tk.StringVar()
        self.search_conditon4 = ttk.Combobox(self,
                                             width=10,
                                             textvariable=
                                             self.search_conditon_choice4)
        self.search_conditon4['values'] = ('降序', '升序')
        self.search_conditon4.place(relx=0.55, rely=0.15)

        self.btn = tk.Button(self, text='开始排序', bg=bt_bg,
                             font=bt_font, command=self.sub)
        self.btn.place(relx=0.75, rely=0.14)
        # 设置文本框
        self.text = tk.Text(self, width=73, height=18,
                            font=bt_font)
        self.text.place(relx=0.1, rely=0.25)




        self.mainloop()
    def sub(self):
        dic = {'序号': 'id', '书名': 'title', '作者': 'author',
               '出版社': 'press', '类别': 'category'}
        key1,value1 = self.search_conditon.get(),self.search_conditon2.get()
        key2,value2 = self.search_conditon3.get(),self.search_conditon4.get()
        if key1==key2:
            showinfo('提示','组合字段不能相同!')
            return None
        sql = None
        if value1==value2=='降序':
            print('降序')
            sql = f'select * from books order by "{dic.get(key1)}" desc,"{dic.get(key2)}" desc'
        elif value1=='降序' and value2=='升序':
            sql = f'select * from books order by "' \
                  f'{dic.get(key1)}" desc,"{dic.get(key2)}"'
        elif value1==value2=='升序':
            sql = f'select * from books order by "' \
                  f'{dic.get(key1)}","{dic.get(key2)}"'
        elif value1=='升序' and value2=='降序':
            sql = f'select * from books order by "' \
                  f'{dic.get(key1)}","{dic.get(key2)}" desc'
        if sql:
            data = self.cursor.execute(sql).fetchall()
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, '序号' + '\t\t' +
                             '书名' + '\t\t' + '作者' +
                             '\t\t' + '出版社' + '\t\t' + '类别')
            for i in data:
                i = [str(j) for j in i]
                self.text.insert(tk.END, '\n')
                self.text.insert(tk.END, '\t\t'.join(i))





if __name__=='__main__':
    Sort().mainloop()




