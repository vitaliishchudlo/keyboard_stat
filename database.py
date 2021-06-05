import pymysql
import json

connection = pymysql.connect(
    host='localhost',
    user='root',
    database='keyboard',
    password=''
)
cursor = connection.cursor()

def get_from_db(user_id):
    pass

def information_operations():
    pass

def send_data():
    pass

