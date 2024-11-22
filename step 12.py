import mysql.connector as m

connect = m.connect(
    host="localhost",
    user="root",
    password="Nhfattyboy96!",
    db="menagerie",
    allow_local_infile=True
)

cursor = connect.cursor()
cursor.execute('DESCRIBE pet')
struc = cursor.fetchall()

for des in struc:
    print(des)

cursor.close()
connect.close()
