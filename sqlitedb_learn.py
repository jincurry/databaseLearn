#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3
import os, sys

def initialize(conn):
    c = conn.cursor()
    c.execute("create table students (sid integer primary key, name text)")
    conn.commit()

def insert(conn, sid, name):
    c = conn.cursor()
    t = (sid, name)
    c.execute("insert into students VALUES (?,?)",t)
    conn.commit()

def delete(conn,sid):
    c = conn.cursor()
    t = (sid,)
    c.execute("delete from students where sid = ?",t)
    conn.commit()

def update(conn, sid, name):
    c = conn.cursor()
    t = (name, sid)
    c.execute("update students set name = ? where sid = ?",t)
    conn.commit()

def display(conn):
    c = conn.cursor()
    c.execute("select * from students")
    print(c.fetchall())

db_name = "test1.db"
conn = sqlite3.connect(db_name)

initialize(conn)

print("insert 3 records")

insert(conn, 1, "Alice")
insert(conn, 2, "Bob")
insert(conn, 3, "Peter")

print("All records:")
display(conn)

print("delete second record")
delete(conn, 2)

print("now, All records:")
display(conn)

print("update the record which sid = 3")
update(conn, 3, "Mark")

print("After update:")
display(conn)

conn.close()