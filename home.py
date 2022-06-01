#  _*_ coding:   utf-8 _*_
import tkinter as tk
from tkinter import filedialog
from config import bt_font, bg, bt_bg
import tkinter.ttk as ttk
import csv
from model import db,cursor
import math
from tkinter.messagebox import showinfo
from change import Change
from add import Add
from static import StaticMain
from sort import Sort

class Home(tk.Tk):
    def __init__(self):
        super(Home, self).__init__()
        self.db = db
        self.cursor = cursor
        self.create()
        self.mainloop()

    # 初始化布局
    def create(self):
        self.geometry('750x500+300+100')
        self.title('系统主页')
        self.configure(bg=bg)
        # 创建菜单栏
        self.menu = tk.Menu(self)
        self.menu.add_command(label='录入',command=self.add)
        self.menu.add_command(label='排序',command=lambda :Sort())
        self.menu.add_command(label='统计',command= lambda :StaticMain())
        self.menu.add_command(label='保存', command=self.save )
        self.config(menu=self.menu)
        # 添加分割线
        self.label1 = tk.Label(self,width=1200,bg='white',height=1)
        self.label1.place(relx=0,rely=0.08)
        self.label2 = tk.Label(self,width=1200,bg=bg,height=1)
        self.label2.place(relx=0,rely=0.084)
        # 查询
        self.condition_label = tk.Label(self,text='请选择查询条件:',bg=bg,font=bt_font)
        self.condition_label.place(relx=0.1,rely=0.018)
        # 设置条件下拉框
        self.search_conditon_choice = tk.StringVar()
        self.search_conditon = ttk.Combobox(self,
                                            width=10,
                                            textvariable=
                                            self.search_conditon_choice)
        self.search_conditon['values'] = ('书名','作者','出版社','类别')
        self.search_conditon_choice.set('书名')
        self.search_conditon.place(relx=0.25,rely=0.019)
        self.search_value = tk.Label(self,text='请输入查询内容:',bg=bg,font=bt_font)
        self.search_value.place(relx=0.4,rely=0.018)
        self.input_search = ttk.Entry(self)
        self.input_search.place(relx=0.55,rely=0.018)

        self.search_btn = tk.Button(self,text='查询',bg=bt_bg,font=bt_font,command=self.search)
        self.search_btn.place(relx=0.78,rely=0.01)
        # 创建侧边栏按钮
        self.c_frame = tk.Frame(self,bg=bg)
        self.show_btn = tk.Button(self.c_frame,text='显示全部书籍',font=bt_font,bg=bt_bg,command=self.show_all)
        self.show_btn.grid(row=1,column=1,pady=20)
        self.delete_btn = tk.Button(self.c_frame, text='删除选中书籍',command=self.select,
                                  font=bt_font, bg=bt_bg,
                               )
        self.delete_btn.grid(row=2, column=1)
        self.change_btn = tk.Button(self.c_frame,
                                    text='修改选中书籍',
                                    font=bt_font, bg=bt_bg,command=self.change
                                    )
        self.change_btn.grid(row=3, column=1,pady=20)

        self.c_frame.place(relx=0.05,rely=0.2)

        # 创建表格
        self.page_index=0
        self.total = 0
        self.max_page = None
        self.table_frame = tk.Frame(bg=bg)
        self.current_page = tk.Label(self.table_frame,
                                     text=f'共{self.total}条记录,每页15条，当前第{self.page_index}页',bg=bg,)
        self.current_page.place(relx=0,rely=0.95)
        columns = ('id',
        'title', 'author', 'press','category')
        self.tree_view = ttk.Treeview(self.table_frame,
                                  show="headings",height=15,
                                  columns=columns)
        # 设置列名
        self.tree_view.column('id', width=50,
                              anchor='center')
        self.tree_view.column('title', width=120,
                          anchor='center')
        self.tree_view.column('author', width=150,
                          anchor='center')
        self.tree_view.column('press', width=120,
                          anchor='center')
        self.tree_view.column('category', width=60,
                          anchor='center')
        # 设置列名显示的文字
        self.tree_view.heading('id', text='序号')
        self.tree_view.heading('title', text='书名')
        self.tree_view.heading('author', text='作者')
        self.tree_view.heading('press', text='出版社')
        self.tree_view.heading('category', text='类别')
        self.tree_view.pack(pady=30, fill=tk.BOTH,
                            expand=True)
        style_value = ttk.Style()
        style_value.configure("Treeview", rowheight=20,
                              font=("微软雅黑", 12))
        # 上一页
        self.last_btn = tk.Button(self.table_frame,text='上一页',bg=bt_bg,command=self.last_btn_click)
        self.last_btn.place(relx=0.6, rely=0.93)
        # 下一页
        self.last_btn = tk.Button(self.table_frame,
                                  text='下一页', bg=bt_bg,
                                  command=self.next_btn_click)
        self.last_btn.place(relx=0.8, rely=0.93)
        self.table_frame.place(relx=0.3, rely=0.1)
        # 绑定选中事件
        self.tree_view.bind('<<TreeviewRelease>>',
                            self.select)
        # 退出提示
        self.protocol('WM_DELETE_WINDOW', self.exit)

    # 书籍信息保存
    def save(self):
        path = filedialog.askdirectory()
        if path:
            data = self.cursor.execute(
                'select * from books').fetchall()
            with open(path+'/books.csv','w',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['序号','书名','出版社','作者','类别'])
                writer.writerows(data)
                showinfo('提示','书籍信息保存成功!')

    # 录入信息
    def add(self):
        Add()
    # 查询信息
    def search(self):
        condition = self.search_conditon.get()
        value = self.input_search.get()
        dic = {'书名':'title','作者':'author','出版社':'press','类别':'category'}
        condition = dic.get(condition)
        sql = f'select * from books where "{condition}" like "%{value}%"'
        data = self.cursor.execute(sql).fetchall()

        self.data=data
        self.page_index = 1
        self.total = len(self.data)
        self.max_page = math.ceil(self.total / 15)
        self.current_page.configure(
            text=f'共{self.total}条记录,每页15条，当前第{self.page_index}页')
        self.tree_show(self.data)

    # 加载全部数据
    def show_all(self):
        self.page_index=1

        self.data = self.cursor.execute('select * from books').fetchall()
        self.total = len(self.data)
        self.max_page = math.ceil(self.total/15)
        self.current_page.configure(text=f'共{self.total}条记录,每页15条，当前第{self.page_index}页')
        show_data = self.data[:15]
        self.tree_show(show_data)

    # tree清空
    def delete_tree(self):
        obj = self.tree_view.get_children()  # 获取所有对象
        for o in obj:
            self.tree_view.delete(o)

    # tree显示数据
    def tree_show(self, data):
        self.delete_tree()
        for index, book in enumerate(data):
            self.tree_view.insert('', index + 1,
                                  values=(
                                      book[0], book[1],
                                      book[2],
                                      book[3], book[4],
                                  ))

    # 点击上一页响应
    def last_btn_click(self):
        if self.page_index>1:
            self.page_index -= 1
            data = self.data[(self.page_index-1)*15:self.page_index*15]
            self.tree_show(data)
            self.current_page.configure(
                text=f'共{self.total}条记录,每页15条，当前第'
                     f'{self.page_index}页')
    # 点击下一页
    def next_btn_click(self):
        if not self.max_page :
            return None
        if self.page_index<self.max_page:
            self.page_index += 1
            data = self.data[(self.page_index - 1) * 15:self.page_index * 15]

            self.current_page.configure(
                text=f'共{self.total}条记录,每页15条，当前第{self.page_index}页')
            self.tree_show(data)
    # 删除选中
    def select(self, *args):
        for item in self.tree_view.selection():
            a = self.tree_view.item(item)['values'][0]
            for i in self.data:
                if i[0] == a:
                    ok = tk.messagebox.askokcancel('提示',f'是否删除{i[1]}?',
                    )
                    if ok:
                        self.cursor.execute(
                            f"delete from books "
                            f"where "
                            f"id='%s';" % a)
                        self.db.commit()
                        self.tree_view.delete(item)
                        tk.messagebox.showinfo(title='温馨提示',
                                           message=f'{i[1]}的信息删除完毕！')
                        self.show_all()
                    else:
                        return None

    # 修改选中
    def change(self, *args):
        for item in self.tree_view.selection():
            a = self.tree_view.item(item)['values']
            id = a[0]
            title = a[1]
            author = a[2]
            press= a[3]
            category = a[4]
            self.change_root = Change()
            self.change_root.booktitle.insert(0,title)
            self.change_root.bookauthor.insert(0,author)
            self.change_root.bookpress.insert(0,press)
            self.change_root.category_choice.set(category)
            dic={'小说':0,'专业书':1,'工具书':2,'报告':3,'其他':4}
            self.change_root.category_conditon.current(dic.get(category))
            self.change_root.id = id
            self.change_root.mainloop()


    # 退出系统
    def exit(self):
        is_exit = tk.messagebox.askokcancel('提示','是否退出系统?')
        if is_exit:
            self.destroy()

if __name__=='__main__':
    Home()
