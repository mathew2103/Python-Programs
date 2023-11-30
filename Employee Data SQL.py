import mysql.connector as mysql

mycon = mysql.connect(
    username="root", host="localhost", password="password", database="journal2")
cur = mycon.cursor()

cur.execute("SELECT * FROM EMPLOYEE where Salary>70000")
data = cur.fetchall()
for i in data:
    print(i)
