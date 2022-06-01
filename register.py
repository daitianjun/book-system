import sqlite3
import tkinter as tk
from tkinter import ttk
from config import bt_font, bg, bt_bg, child_size
from tkinter.messagebox import showinfo


class Register(tk.Tk):
    def __init__(self):
        self.db = sqlite3.connect('static/data.db')
        self.cursor = self.db.cursor()
        super(Register, self).__init__()
        self.configure(bg= bg)
        self.title("用户注册")
        self.geometry(child_size)
        # 用户名
        self.name_l = tk.Label(self, text='用户名:',bg=bg,
                               font=bt_font)
        self.name = ttk.Entry(self, )
        # 密码
        self.password_l = tk.Label(self, text='密码:',bg=bg,
                                   font=bt_font)
        self.password = ttk.Entry(self, show='*')
        # 确认密码
        self.password1_l = tk.Label(self,
                                    text='确认密码:',bg=bg,
                                    font=bt_font)
        self.password1 = ttk.Entry(self, show='*')
        # 重置
        self.rt = tk.Button(self, text='重置',
                            command=self.reset,font=bt_font,bg=bt_bg)
        # 提交注册
        self.st = tk.Button(self, text='提交',
                            command=self.submit,font=bt_font,bg=bt_bg)

        self.name_l.grid(row=1,column=1,padx=40,pady=20)
        self.name.grid(row=1,column=2)
        self.password_l.grid(row=2,column=1,)
        self.password.grid(row=2,column=2)
        self.password1_l.grid(row=3,column=1,pady=20)
        self.password1.grid(row=3,column=2)
        self.rt.grid(row=4,column=1)
        self.st.grid(row=4,column=2)

        self.mainloop()



    def reset(self):
        self.name.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.password1.delete(0, tk.END)

    # 提交注册按钮
    def submit(self):

        name = self.name.get()  # 获取用户名
        password = self.password.get()  # 获取密码
        password1 = self.password1.get()  # 再次获取密码
        if name=='' or password == '' or password1 == '':
            showinfo('提示','注册信息不能为空!')
            return None
        if password != password1:
            showinfo('提示', '两次密码不一致!')
            return None
        try:
            sql = f'insert into users(username,password) values ("{name}","{password}")'
            self.cursor.execute(sql)
            self.db.commit()
            tk.messagebox.showinfo(title='提示',
                                   message='注册成功')
            self.destroy()
        except Exception as e:
            print(e)
            showinfo('提示', '该用户已经注册过或用户名密码长度过长!')
    def __del__(self):
        self.db.close()


if __name__ == '__main__':
    Register()
