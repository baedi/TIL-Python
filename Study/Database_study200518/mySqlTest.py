import pymysql

print('[MySQL Test]')

# MySQL Connect
connection = pymysql.connect(host='localhost', user='ruser', password='0000', db='TestDatabase2020', charset='utf8')

# Cursor
cursor = connection.cursor()

# SQL Query
sql = "SELECT * FROM table1"
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(str(row[0]) + ' ' + str(row[1]))


# input data
number = input('Your number : ')
name = input('Your name : ')


sql = "INSERT INTO table1 VALUES (%s, '%s')" % (number, name)
cursor.execute(sql)
connection.commit()

print('Success Input data')\

connection.close()
