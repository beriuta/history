# import pymysql
# user = input('请输入用户名:')
# pwd = input('请输入密码:')
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor()
# cursor.close()
# sql = "select * from t1 where username='%s' and password='%s'" % (name, pwd)
# ret = cursor.execute(sql)
# if ret:
#     print('登陆成功')
# else:
#     print('登录失败')
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor()
# sql = "insert into  t1 (username,password) values (%s,%s);"  # 增加
# ret = cursor.execute(sql, ['hanlei', '123'])
# sql = "delete from t1 where username=%s;"  # 删
# ret = cursor.execute(sql, ['hanlei'])
# sql = "update t1 set password=%s where username=%s;"
# ret = cursor.execute(sql, ['567', 'ali'])
# conn.commit()
# cursor.close()
# conn.close()
# import pymysql
# name = input('请输入用户名:')
# pwd = input('请输入密码:')
# conn = pymysql.connect(
#     host='192.168.16.108',
#     port=9000,
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor()    #确认光标
# sql = "delete password from t1 where username=%s;"
# ret = cursor.execute(sql,['ali'])
# print(ret)
# conn.commit()
# cursor.close()
# conn.close()
# import pymysql
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,      #只能用起了服务器的端口号，9000如果也起了服务器就可以
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor()
# sql = "delete from t1 where username=%s;"
# ret = cursor.execute(sql, ['hanlei'])
# conn.commit()
# cursor.close()
# conn.close()
# import pymysql
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor()
# sql = "insert into t1 (username,password) values ('aimei','2345');"
# ret = cursor.execute(sql)
# conn.commit()
# cursor.close()
# conn.close()
# import pymysql
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 获取光标
# sql = "select * from t1;"
# cursor.execute(sql)
# ret = cursor.fetchall()  # 查询所有的表格内容
# print(ret)  # [{'id': 1, 'username': 'ali', 'password': '567'}, {'id': 5, 'username': 'aimei', 'password': '2345'}]
# ret = cursor.fetchone()
# print(ret)  # {'id': 1, 'username': 'ali', 'password': '567'} 第一条
# ret = cursor.fetchone()  # {'id': 5, 'username': 'aimei', 'password': '2345'} 第二条
# print(ret)
# ret = cursor.fetchmany(3)  # 查询三条数据
# print(ret)  # [{'id': 1, 'username': 'ali', 'password': '567'}, {'id': 5, 'username': 'aimei', 'password': '2345'}, {'id': 6, 'username': 'eva', 'password': '432'}]
# ret = cursor.fetchmany(3)
# print(ret)  # [{'id': 1, 'username': 'ali', 'password': '567'}, {'id': 5, 'username': 'aimei', 'password': '2345'}, {'id': 6, 'username': 'eva', 'password': '432'}]
# print(cursor.fetchone())  # {'id': 7, 'username': 'beriu', 'password': '688'}
# print(cursor.fetchone())  # {'id': 8, 'username': 'wei', 'password': '234'}
# print(cursor.fetchone())  # None
# cursor.scroll(1, mode='absolute')  # 绝对位置，移动1
# print(cursor.fetchone())  # {'id': 1, 'username': 'ali', 'password': '567'}
# cursor.scroll(0,mode = 'relative')  # 相对位置，基于光标当前位置移动
# print(cursor.fetchone())
# cursor.close()
# conn.close()
# import pymysql
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor()
# sql = 'select * from t1;'
# cursor.execute(sql)
# ret = cursor.fetchall()  # 默认以元祖的形式打印出来
# print(ret)  # ((1, 'ali', '567'), (5, 'aimei', '2345'), (6, 'eva', '432'), (7, 'beriu', '688'), (8, 'wei', '234'))
# cursor.close()
# conn.close()
# import pymysql
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor()
# sql = "insert into p(name) values('西西出版社');"  # 插入一条数据
# cursor.lastrowid  # 获取刚才插入到数据库的id值
# sql2 = "insert into book(title,p_id) values (%s,%s)"
# conn.rollback()  # 回滚
# conn.commit()
# cursor.close()
# conn.close()
# import pymysql
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     database='day43',
#     charset='utf8'
# )
# cursor = conn.cursor()
# sql = 'insert into user1(name,gae) values(%s,%s);'
# try:
#     cursor.execute(sql, ["ali",'14'])
#     conn.commit()
# except Exception as e:
#     conn.rollback()  # 有异常，触发回滚机制
# cursor.close()
# select sid from student where sid in(
# select s1.student_id from score as s1,score as s2
# where s1.student_id=s2.student_id and s1.course_id=1 and s2.course_id=2 and s1.num > s2.num
# );
# mysql> select course_id,max(number),min(number) from score group by course_id;
# mysql> select sid,sname from student where sid in
# ( select student_id from score group by student_id having count(course_id)=1);
# mysql> select sid,sname from student where sid=2;
# mysql> select student_id from score where course_id in (1,2) and student_id !=1;
# mysql> select student_id from score where course_id in (1,2);
# mysql> select course_id from score where student_id=1;
# mysql> select sid,sname from student where sid = (select student_id from score where number <60);
# mysql> select course_id,avg(number) from score group by course_id order by avg(number) desc;
# select gender,count(sid) from student group by gender;



