# from threading import Thread, Lock, Condition
# import sys
# from win32api import LoadKeyboardLayout
# import keyboard
# import time
#
# class App:
#     def __init__(self):
#         self.list = list()
#         self.paused = False
#         self.state = Condition()
#
#     def keyboard_hook(self):
#         print('hook')
#         keyboard.hook(self.key_logger)
#         keyboard.wait()
#
#     def start(self):
#
#         th1 = Thread(target=self.send_data, args=())
#         th1.start()
#         print('start1')
#
#         self.th1 = th1
#         self.keyboard_hook()
#         print('start2')
#         time.sleep(4)
#
#
#
#     def key_logger(self, e):
#         print('pres')
#         if e.event_type == 'up':
#             print(f'You pressed: {e.name}')
#         else:
#             pass
#
#
#
#     def send_data(self):
#         print('i am here')
#         time.sleep(1.5)
#         self.send_data()
#
# if __name__ == '__main__':
#     LoadKeyboardLayout('00000409', 1)
#     App().start()


arr = ['a', 's', 'd', '1', 's', 'd', 'w', 'e', 'q']
arr2 = ['=', 'w', 'r', 'p', 'f', ';', 'a', 'e', 'e', '[', 'w', 'q', 'r', "'", 'q', 'r', '3', 'caps lock', ';',
        'D', 'A', 'S', 'D', 'shift', 'alt', 'ctrl', 'F', '.', 'C', 'F', 'R', 'D', 'shift', 'alt', 'D', 'shift']
arr2_len = len(arr2)
print(arr2_len)




res = dict((i, arr2.count(i)) for i in arr2)
print(len(res))

print(res)
