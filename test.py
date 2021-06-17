# arr = ['a', 's', 'd', '1', 's', 'd', 'w', 'e', 'q', 'shift']
# arr2 = ['=', 'w', 'r', 'p', 'f', ';', 'a', 'e', 'e', '[', 'w', 'q', 'r', "'", 'q', 'r', '3', 'caps lock', ';',
#         'D', 'A', 'S', 'D', 'shift', 'alt', 'ctrl', 'F', '.', 'C', 'F', 'R', 'D', 'shift', 'alt', 'D', 'shift', 'shift']
# arr2_len = len(arr2)
# print(arr2_len)
# print('\n\n')

# res = dict((i, arr2.count(i)) for i in arr2)
# print(len(res))
#
# print('\n\n')
# print(res)


# from collections import Counter
#
# a = {'a': 4, 'b': 3, 'c': 8}
# b = {'a': 1, 'b': 4}
# z = {'[': 3, 'shift': 3}
#
# c = Counter()
# for d in a, b, z:
#     c.update(d)
# print(c)


# list = ['3', '#', 'shift', '3', '%', 'b', '5']
#
# dic = {'#': '3', '%': '5'}
#
# print([dic.get(n, n) for n in list])


# work
# a = [1, 2, 3, 4, 1, 5, 3, 2, 6, 1, 1]
# dic = {1:10, 2:20, 3:'foo'}
#
# print([dic.get(n, n) for n in a]

#104 znaku
import json
import pymysql

connection = pymysql.connect(
    host='remotemysql.com',
    user='JrsFeohzhH',
    database='JrsFeohzhH',
    password='mY9ZPqKMe3'
)
cursor = connection.cursor()
date = {
    'special': {
        'esc': 0,
        'tab': 0,
        'caps lock': 0,

        'left shift': 0,
        'left ctrl': 0,
        'left windows': 0,
        'left alt': 0,

        'right alt': 0,
        'right windows': 0,
        'right ctrl': 0,
        'right shift': 0,

        'enter': 0,
        'backspace': 0,
        'delete': 0,
        'insert': 0,
        'print screen': 0,
        'scroll lock': 0,
        'pause': 0
    },
    'text': {
        '~': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '0': 0,
        '-': 0,
        '=': 0,
        'q': 0,
        'w': 0,
        'e': 0,
        'r': 0,
        't': 0,
        'y': 0,
        'u': 0,
        'i': 0,
        'o': 0,
        'p': 0,
        '[': 0,
        ']': 0,
        '\\': 0,
        'a': 0,
        's': 0,
        'd': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        ';': 0,
        '\'': 0,
        'z': 0,
        'x': 0,
        'c': 0,
        'v': 0,
        'b': 0,
        'n': 0,
        'm': 0,
        ',': 0,
        '.': 0,
        '/': 0,
        'space': 0
    },
    'functional': {
        'f1': 0,
        'f2': 0,
        'f3': 0,
        'f4': 0,
        'f5': 0,
        'f6': 0,
        'f7': 0,
        'f8': 0,
        'f9': 0,
        'f10': 0,
        'f11': 0,
        'f12': 0
    },
    'cursor': {
        'left': 0,
        'right': 0,
        'down': 0,
        'up': 0,
        'end': 0,
        'home': 0,
        'page down': 0,
        'page up': 0
    },
    'additional': {
        'numpad_0': 0,
        'numpad_1': 0,
        'numpad_2': 0,
        'numpad_3': 0,
        'numpad_4': 0,
        'numpad_5': 0,
        'numpad_6': 0,
        'numpad_7': 0,
        'numpad_8': 0,
        'numpad_9': 0,
        'numpad_decimal': 0,
        'numpad_enter': 0,
        'numpad_plus': 0,
        'numpad_minus': 0,
        'numpad_multiply': 0,
        'numpad_divide': 0,
        'numpad_num lock': 0
    }
}

sql = 'UPDATE dkp__2021_June SET day_1=%s WHERE id_user=%s'

val = (json.dumps(date), 3333)

result = cursor.execute(sql, val)
connection.commit()

print(result)
print('\\')
# import pymysql
#
# connection = pymysql.connect(
#     host='remotemysql.com',
#     user='JrsFeohzhH',
#     database='JrsFeohzhH',
#     password='f9Sex6J7vk'
# )
#
a = {
    'special': {
        'esc': 0,
        'tab': 0,
        'caps lock': 0,

        'left shift': 0,
        'left ctrl': 0,
        'left windows': 0,
        'left alt': 0,

        'right alt': 0,
        'right windows': 0,
        'right ctrl': 0,
        'right shift': 0,

        'enter': 0,
        'backspace': 0,
        'delete': 0,
        'insert': 0,
        'print screen': 0,
        'scroll lock': 0,
        'pause': 0
    },
    'text': {
        '~': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '0': 0,
        '-': 0,
        '=': 0,
        'q': 0,
        'w': 0,
        'e': 0,
        'r': 0,
        't': 0,
        'y': 0,
        'u': 0,
        'i': 0,
        'o': 0,
        'p': 0,
        '[': 0,
        ']': 0,
        '\\': 0,
        'a': 0,
        's': 0,
        'd': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        ';': 0,
        '\'': 0,
        'z': 0,
        'x': 0,
        'c': 0,
        'v': 0,
        'b': 0,
        'n': 0,
        'm': 0,
        ',': 0,
        '.': 0,
        '/': 0,
        'space': 0
    },
    'functional': {
        'f1': 0,
        'f2': 0,
        'f3': 0,
        'f4': 0,
        'f5': 0,
        'f6': 0,
        'f7': 0,
        'f8': 0,
        'f9': 0,
        'f10': 0,
        'f11': 0,
        'f12': 0
    },
    'cursor': {
        'left': 0,
        'right': 0,
        'down': 0,
        'up': 0,
        'end': 0,
        'home': 0,
        'page down': 0,
        'page up': 0
    },
    'additional': {
        'numpad_0': 0,
        'numpad_1': 0,
        'numpad_2': 0,
        'numpad_3': 0,
        'numpad_4': 0,
        'numpad_5': 0,
        'numpad_6': 0,
        'numpad_7': 0,
        'numpad_8': 0,
        'numpad_9': 0,
        'numpad_decimal': 0,
        'numpad_enter': 0,
        'numpad_plus': 0,
        'numpad_minus': 0,
        'numpad_multiply': 0,
        'numpad_divide': 0,
        'numpad_num lock': 0
    }
}






