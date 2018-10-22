'''
1、查询男生、女生的人数；
select gender,count(sid) from student group by gender;
+--------+------------+
| gender | count(sid) |
+--------+------------+
| 女     |          2 |
| 男     |          1 |
+--------+------------+
2 rows in set (0.00 sec)

2、查询姓“张”的学生名单；
mysql> select * from student where sname like '张';
Empty set (0.00 sec)

3、课程平均分从高到低显示
mysql> select course_id,avg(number) from score group by course_id order by avg(number) desc;
+-----------+-------------+
| course_id | avg(number) |
+-----------+-------------+
|         2 |     79.5000 |
|         1 |     60.0000 |
+-----------+-------------+
2 rows in set (0.00 sec)

4、查询有课程成绩小于60分的同学的学号、姓名；
mysql> select sid,sname from student where sid = (select student_id from score where number <60);
+-----+--------+
| sid | sname  |
+-----+--------+
|   1 | 钢弹   |
+-----+--------+
1 row in set (0.00 sec)

5、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；
mysql> select course_id from score where student_id=1;
+-----------+
| course_id |
+-----------+
|         1 |
|         2 |
+-----------+
2 rows in set (0.00 sec)

mysql> select student_id from score where course_id in (1,2);
+------------+
| student_id |
+------------+
|          1 |
|          1 |
|          2 |
+------------+
3 rows in set (0.00 sec)

mysql> select student_id from score where course_id in (1,2) and student_id !=1;
+------------+
| student_id |
+------------+
|          2 |
+------------+
1 row in set (0.00 sec)

mysql> select sid,sname from student where sid=2;
+-----+--------+
| sid | sname  |
+-----+--------+
|   2 | 铁锤   |
+-----+--------+
1 row in set (0.00 sec)

6、查询出只选修了一门课程的全部学生的学号和姓名；
mysql> select sid,sname from student where sid in ( select student_id from score group by student_id having count(course_id)=1);
+-----+--------+
| sid | sname  |
+-----+--------+
|   2 | 铁锤   |
+-----+--------+
1 row in set (0.00 sec)


7、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
mysql> select course_id,max(number),min(number) from score group by course_id;
+-----------+-------------+-------------+
| course_id | max(number) | min(number) |
+-----------+-------------+-------------+
|         1 |          60 |          60 |
|         2 |         100 |          59 |
+-----------+-------------+-------------+
2 rows in set (0.00 sec)

8、查询课程编号“2”的成绩比课程编号“1”成绩低的所有同学的学号、姓名；
select sid,sname from student where sid in(
select s1.student_id from score as s1,score as s2
where s1.student_id=s2.student_id and s1.course_id=1 and s2.course_id=2 and s1.num > s2.num
);

9、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
select sid from student where sid in(
select s1.student_id from score as s1,score as s2
where s1.student_id=s2.student_id and s1.course_id=1 and s2.course_id=2 and s1.num > s2.num
);
10、查询平均成绩大于60分的同学的学号和平均成绩;

11、查询所有同学的学号、姓名、选课数、总成绩；

12、查询姓“李”的老师的个数；

13、查询没学过“张磊老师”课的同学的学号、姓名；

14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；

15、查询学过“李平老师”所教的所有课的同学的学号、姓名；
'''