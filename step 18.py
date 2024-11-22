import mysql.connector as m

connect = m.connect(
    host="localhost",
    user="root",
    password="Nhfattyboy96!",
    db="menagerie",
    allow_local_infile=True
)

cursor = connect.cursor()
query = "SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'"
cursor.execute(query)
female_dogs = cursor.fetchall()

print("Records of Female Dogs:")
print("-------------------------------")
for record in female_dogs:
    print(record)

cursor.close()
connect.close()
