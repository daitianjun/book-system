import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import tkinter.messagebox
from config import bt_font, bg, bt_bg
from home import Home
from register import Register


class Login(tk.Tk):
    def __init__(self, ):
        super(Login, self).__init__()
        self.db = sqlite3.connect('static/data.db')
        self.cursor = self.db.cursor()
        self.configure(bg=bg)
        self.title('个人书籍管理系统——用户登录')
        self.creat()
        self.mainloop()

    def __del__(self):
        self.db.close()

    # 基本布局
    def creat(self):
        self.geometry('750x500+300+100')

        # 加载主页图片
        self.image = ImageTk.PhotoImage(
            file='static/bg.jpg')
        self.photo_label = tk.Label(self,
                                    image=self.image,
                                    width=750, height=420)
        self.photo_label.pack()
        # 用户名
        self.label2 = tk.Label(self, text='请输入用户名:', bg=bg,
                               font=bt_font
                               )
        self.label2.place(relx=0.02, rely=0.9, )
        self.input1 = ttk.Entry(self, )
        self.input1.place(relx=0.15, rely=0.9)
        self.botton = tk.Button(text='注册', font=bt_font,
                                bg=bt_bg, command=Register)
        self.botton.place(relx=0.85, rely=0.89)
        # 密码
        self.label3 = tk.Label(self, text='请输入密码:', bg=bg,
                               font=bt_font)
        self.label3.place(relx=0.38, rely=0.9, )
        self.input2 = ttk.Entry(self, show='*')
        self.input2.place(relx=0.5, rely=0.9)
        self.botton1 = tk.Button(self, text='登录',
                                 command=self.login,
                                 font=bt_font, bg=bt_bg)

        self.botton1.place(relx=0.75, rely=0.89)
        self.resizable(False, False)

    # 登录
    def login(self):
        username = self.input1.get()
        password = self.input2.get()
        print(username, password)
        if username == '' or password == '':
            tk.messagebox.showerror('登录失败',
                                    message='用户名或者密码不能为空')
            return None

        sql = f'select * from users where username="' \
              f'{username}" and password="{password}";'
        data = self.cursor.execute(sql).fetchall()
        if data == []:
            tk.messagebox.showerror('登录失败', '用户名或密码错误!')
        else:
            self.destroy()
            Home()


if __name__ == '__main__':
    Login()
