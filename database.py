import pymysql
import json

connection = pymysql.connect(
    host='localhost',
    user='root',
    database='keyboard',
    password=''
)
cursor = connection.cursor()
x = {
    "name": "Viktor",
    "age": {
        'main': 30,
        'second': 12
    },
    "city": "Minsk"
}

j = json.dumps(x)

d = 'da'

sql = 'INSERT INTO user_data(login, password) VALUES (%s, %s)'
val = (x, d)

print(cursor.execute(sql, val))


print(j)

connection.commit()
