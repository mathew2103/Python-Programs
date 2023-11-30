import mysql.connector as mysql

mycon = mysql.connect(
    username="root", host="localhost", password="password", database="journal2"
)
cur = mycon.cursor()
cur.execute("UPDATE EMPLOYEE SET SALARY=SALARY+2000 where SALARY<50000")
mycon.commit()
print("Updated!")
