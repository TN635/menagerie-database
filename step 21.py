import mysql.connector as m

connect = m.connect(
    host="localhost",
    user="root",
    password="Nhfattyboy96!",
    db="menagerie",
    allow_local_infile=True
)

cursor = connect.cursor()
query = "SELECT name, birth FROM pet"
cursor.execute(query)
nam_birth = cursor.fetchall()

print("Records of name and birth column:")
print("-------------------------------")
for record in nam_birth:
    print(record)

cursor.close()
connect.close()
