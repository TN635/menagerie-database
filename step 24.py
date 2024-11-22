import mysql.connector as m

connect = m.connect(
    host="localhost",
    user="root",
    password="Nhfattyboy96!",
    db="menagerie",
    allow_local_infile=True
)

cursor = connect.cursor()
query = "SELECT owner, COUNT(*) AS count_pet FROM pet GROUP BY owner"
cursor.execute(query)
pet_count = cursor.fetchall()

print("Pet number for owners:")
print("-------------------------------")
for record in pet_count:
    print(record)

cursor.close()
connect.close()
