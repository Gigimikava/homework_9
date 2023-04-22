#1
import sqlite3
conn = sqlite3.connect("customers.sqlite")
cursor=conn.cursor()

# #2
# select_result = cursor.execute("SELECT * FROM users")
# rows=cursor.fetchall()
# for row in rows:
#     print(row[1],row[5])

# #3
# select_result=cursor.execute("SELECT * FROM users WHERE age > 25")
# for row in select_result:
#     print(row[2:5])
#
# age = 15
# select_result=cursor.execute("SELECT * FROM users WHERE age > ?",(age,))
# for row in select_result:
#     print(row[2],row[3],row[4])

# #4
# select_result=cursor.execute("SELECT * FROM users WHERE age BETWEEN 10 AND 25")
# for row in select_result:
#     print(row)

# #5
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
# select_result=cursor.execute("SELECT * FROM users WHERE age <> 20")
# for row in select_result:
#     print(row["firstname"],row["lastname"])

#6

# #N7
# select_result=cursor.execute("SELECT * FROM users order by age desc")
# for row in select_result:
#     print(tuple(row))

# #8
# select_result=cursor.execute("SELECT DISTINCT firstname FROM users order by age")
# for row in select_result:
#     print(row[0])

# #9
# select_result=cursor.execute("UPDATE users SET username = 'noobmaster' WHERE age = 20 ")
# print(cursor.rowcount)
# conn.commit()

# #10
# select_result=cursor.execute("UPDATE users SET age = 15 WHERE age > 30 ")
# print(cursor.rowcount)
# conn.commit()

# #11
# select_result=cursor.execute("DELETE FROM users where user_id = 5")
# print(cursor.rowcount)
# conn.commit()

# #12
# select_result=cursor.execute("DELETE FROM users where firstname like 'ა%'")
# print(cursor.rowcount)
# conn.commit()


conn.close()