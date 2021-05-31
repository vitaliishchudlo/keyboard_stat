# arr = ['a', 's', 'd', '1', 's', 'd', 'w', 'e', 'q', 'shift']
# arr2 = ['=', 'w', 'r', 'p', 'f', ';', 'a', 'e', 'e', '[', 'w', 'q', 'r', "'", 'q', 'r', '3', 'caps lock', ';',
#         'D', 'A', 'S', 'D', 'shift', 'alt', 'ctrl', 'F', '.', 'C', 'F', 'R', 'D', 'shift', 'alt', 'D', 'shift', 'shift']
# arr2_len = len(arr2)
# print(arr2_len)
# print('\n\n')
#
#
#
# res = dict((i, arr2.count(i)) for i in arr2)
# print(len(res))
#
# print('\n\n')
# print(res)


import requests, time
import plyer

url = 'http://au.nung.edu.ua/index.php?subj=85'

request1 = requests.get(url)
result1 = request1.text

while True:
        url2 = 'http://au.nung.edu.ua/index.php?subj=85'
        request2 = requests.get(url2)
        result2 = request2.text
        if result1 == result2:
                print('The test is busy!')
                time.sleep(1.3)
        else:
                print('The test is free!\n\nЙДИ ПРОХОДИ')

                time.sleep(0.3)

