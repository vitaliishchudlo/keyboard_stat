import win32api
import keyboard
import datetime


class MainFunc:
    tm = "0"
    dir = []
    #to delete
    
    def __init__(self):
        keyboard.hook(self.pressed_key)
        keyboard.wait()

    def pressed_key(self, e):
        res = e.name  # названия кнопки, например 'enter', 'caps lock'
        if e.event_type == 'up':
            tm_now = str(datetime.datetime.now().time())[:-10]
            print(tm_now)


            if self.tm != tm_now:
                self.tm = tm_now
                self.dir.append(res)
                print(res)
                print(self.dir)
                            # print('Zapros bd')
                            # print(self.dir)
                            # item = 'a'
                            # if item in self.dir:
                            #     print('PISKA')
                #self.dir.clear()  !!!!!!!!!

            else:
                self.dir.append(res)
                print(res)
                print(self.dir)
                            # print(self.dir)
                            # print(res)
                            # print("время не меняется")


if __name__ == '__main__':
    win32api.LoadKeyboardLayout('00000409', 1)
    MainFunc()


