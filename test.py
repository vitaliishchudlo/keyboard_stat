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


#work
# a = [1, 2, 3, 4, 1, 5, 3, 2, 6, 1, 1]
# dic = {1:10, 2:20, 3:'foo'}
#
# print([dic.get(n, n) for n in a]