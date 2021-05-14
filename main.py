from threading import Thread, Lock, Condition
import sys
from win32api import LoadKeyboardLayout
import keyboard
import time

class App:
    def __init__(self):
        self.list = list()
        self.paused = False
        self.state = Condition()

    def keyboard_hook(self):
        keyboard.hook(self.key_logger)
        keyboard.wait()

    def start(self):

        th1 = Thread(target=self.send_data, args=())
        th1.start()


        self.th1 = th1
        self.keyboard_hook()
        time.sleep(4)



    def key_logger(self, e):
        res = e.name
        if res == 'enter':
            print('exiting..')
            self.paused = True
            sys.exit()
        else:
            if e.event_type == 'up':
                print(f'You pressed: {res}')
            else:
                pass


    def send_data(self):
        with self.state:
            if self.paused is True:
                self.state.wait()
            else:
                print('i am here')
                time.sleep(3)
                self.send_data()








if __name__ == '__main__':
    LoadKeyboardLayout('00000409', 1)
    App().start()













# import win32api
# import keyboard
# import datetime
#
#
# class MainFunc:
#     tm = "0"
#     dir = []
#     #to delete
#
#     def __init__(self):
#         keyboard.hook(self.pressed_key)
#         keyboard.wait()
#
#     def pressed_key(self, e):
#         res = e.name  # названия кнопки, например 'enter', 'caps lock'
#         if e.event_type == 'up':
#             tm_now = str(datetime.datetime.now().time())[:-10]
#             print(tm_now)
#
#
#             if self.tm != tm_now:
#                 self.tm = tm_now
#                 self.dir.append(res)
#                 print(res)
#                 print(self.dir)
#                             # print('Zapros bd')
#                             # print(self.dir)
#                             # item = 'a'
#                             # if item in self.dir:
#                             #     print('PISKA')
#                 #self.dir.clear()  !!!!!!!!!
#
#             else:
#                 self.dir.append(res)
#                 print(res)
#                 print(self.dir)
#                             # print(self.dir)
#                             # print(res)
#                             # print("время не меняется")
#
#
# if __name__ == '__main__':
#     win32api.LoadKeyboardLayout('00000409', 1)
#     MainFunc()
#
#
