import mysql.connector as m

connect = m.connect(
    host="localhost",
    user="root",
    password="Nhfattyboy96!"
)

cursor = connect.cursor()
cursor.execute("DROP DATABASE IF EXISTS menagerie")
cursor.execute('SHOW DATABASES')
data = cursor.fetchall()

for db in data:
    print(db)

cursor.close()
connect.close()
