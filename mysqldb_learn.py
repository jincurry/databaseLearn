#!/usr/bin/env python
import pymysql

db = pymysql.connect('localhost', 'root', '453122', 'test_mysql')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
cursor.execute("drop table if EXISTS employee")
sql = """
        create table employee (first_name char(20) not NULL, last_name CHAR(20),
        age INT, sex char(1), income FLOAT)
        """
cursor.execute(sql)

sqlSequence = []

sql1 = """
        INSERT INTO employee(first_name,last_name,age,sex,income)
        VALUES ("Mac", "curry", 20, 'M', 4000)
        """
sqlSequence.append(sql1)

sql2 = """
        INSERT INTO employee(first_name,last_name,age,sex,income)
        VALUES ("Jimmy", "Bob", 22, 'F', 3000)
        """
sqlSequence.append(sql2)

sql3 = """
        INSERT INTO employee(first_name,last_name,age,sex,income)
        VALUES ("Peter", "Green", 21, 'M', 4050)
        """
sqlSequence.append(sql3)

sql4 = """
        INSERT INTO employee(first_name,last_name,age,sex,income)
        VALUES ("Ken", "Alice", 24, 'F', 2000)
        """
sqlSequence.append(sql4)

for sql in sqlSequence:
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

print("database version is {0}".format(data))
try:
    result = cursor.execute("select * from employee")
    print(result)
    for i in range(result):
        print(cursor.fetchone())
    db.commit()
except:
    db.rollback()

# 进行删除操作
sql = "delete from employee where age > {0}".format(23)
try:
    result = cursor.execute(sql)
    print(result)
    # 查看剩下元素
    result = cursor.execute("select * from employee")
    for i in range(result):
        print(cursor.fetchone())
    db.commit()
except:
    db.rollback()

# 进行更新操作
sql = "update employee set age = age + 1 where income = 3000"
try:
    print("updating:")
    result = cursor.execute(sql)
    print(result)
    for i in range(result):
        print(cursor.fetchone())
    db.commit()
except:
    db.rollback()

try:
    print("after updated:")
    result = cursor.execute("select * from employee")
    for i in range(result):
        print(cursor.fetchone())
except:
    print("some error occured!")
db.close()