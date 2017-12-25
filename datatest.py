#! /usr/bin/env python
import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute("create table if not exists students(sid integer primarykey, name text)")
# conn.commit()

c.execute('insert into students VALUES(?,?) ',(1,"Alice"))
c.execute('insert into students VALUES(?,?) ',(2,"Bob"))
c.execute('insert into students VALUES(?,?) ',(3,"Peter"))

c.execute("DELETE FROM students WHERE sid = ?",(1,))
c.execute("UPDATE students SET name = ? WHERE sid = ?",("mark",3))
conn.commit()
c.execute("SELECT * FROM students")
print(c.fetchall())
conn.close()