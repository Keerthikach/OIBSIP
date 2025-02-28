import sqlite3 
from datetime import datetime

conn=sqlite3.connect("bmi_db.db")
cursor=conn.cursor()

query="""
       CREATE TABLE IF NOT EXISTS bmi_recs(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       weight REAL,
       height REAL,
       bmi REAL,
       date TEXT  )
"""
cursor.execute(query)
conn.commit()
conn.close()

def add_recs(name,weight,height,bmi):
    conn=sqlite3.connect("bmi_db.db")
    cursor=conn.cursor()

    date=datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
    query1="INSERT INTO bmi_recs(name,weight,height,bmi,date) VALUES(?,?,?,?,?)"
    cursor.execute(query1,(name,weight,height,bmi,date))  

    conn.commit()
    conn.close()

def display_recs(username):
    conn=sqlite3.connect("bmi_db.db")
    cursor=conn.cursor()  
    cursor.execute("SELECT * FROM bmi_recs WHERE name=?",(username,)) 

    return cursor.fetchall()  

print(display_recs("va;ala"))



    

    

