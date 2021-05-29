from threading import Thread, Lock, Condition
import sys
from win32api import LoadKeyboardLayout
import keyboard
import time


class App():
    def __init__(self):
        pass


    def send_data(self):
        print('sending data first')
        time.sleep(3)

    def start_keylogger(self):
        print('none')


    def check_params(self):
        with open('test.txt', 'r') as file:
            result = file.read()
            if result == 'stop':
                print('stoper')
                time.sleep(1)
                self.check_params()
            else:
                print('working')
                time.sleep(1)
                self.check_params()

        # with open("test.txt", "r") as f:
        #     text = f.read()
        #     if text == '1':
        #         print(f'like: {text}')
        #         time.sleep(1)
        #         self.smel()
        #     else:
        #         sys.exit()

    def run(self):
        th1 = Thread(target=self.start_keylogger)
        th2 = Thread(target=self.send_data)
        th1.start()
        th2.start()

        self.check_params()




        input('\n\nPress ENTER to exit')


if __name__ == '__main__':
    LoadKeyboardLayout('00000409', 1)
    App().run()