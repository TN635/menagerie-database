import mysql.connector as m

connect = m.connect(
    host="localhost",
    user="root",
    password="Nhfattyboy96!",
    db="menagerie",
    allow_local_infile=True
)

cursor = connect.cursor()
cursor.execute("SELECT * FROM pet")
records = cursor.fetchall()

print("Records in the pet table:")
print("-------------------------------")
for record in records:
    print(record)

cursor.close()
connect.close()
