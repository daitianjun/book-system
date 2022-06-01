import random
import sqlite3


'''
此文件创建数据库数据表
'''

db = sqlite3.connect('static/data.db')
cursor = db.cursor()


# 创建书籍表
def create_book_info():
    '''
    id :序号
    title:书名
    author:作者
    press:出版社
    category:类别
    '''
    sql = 'create table if not exists books(id integer primary key AUTOINCREMENT,title VARCHAR (20),author VARCHAR ' \
          '(50),press VARCHAR (20),category varchar (10))'
    cursor.execute(sql)


# 创建用户表
def create_user_info():
    sql = 'create table if not exists users(username ' \
          'VARCHAR(10) primary KEY ,password VARCHAR(20))'
    cursor.execute(sql)

# 添加测试数据
def add_book():
    categorys=['专业书','工具书','报告','小说','其他']

    for i in range(1,50):
        category = random.choice(categorys)
        sql = f"insert into books (id,title,author,press,category)values('{i}','书名{i}','作者{i}','出版社{i}','{category}')"
        cursor.execute(sql)
        print(f'第{i}本书添加成功!')
    db.commit()


if __name__=='__main__':
    create_book_info()
    create_user_info()
    add_book()
