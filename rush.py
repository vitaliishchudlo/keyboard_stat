import win32api
import keyboard
import datetime


class MainFunc:
    tm = "0"
    dir = []

    def __init__(self):
        keyboard.hook(self.pressed_key)
        keyboard.wait()

    def pressed_key(self, e):
        res = e.name  # названия кнопки, например 'enter', 'caps lock'
        if e.event_type == 'up':
            tm_now = str(datetime.datetime.now().time())[:-10]

            if self.tm != tm_now:
                self.tm = tm_now
                self.dir.append(res)
                print('Zapros bd')
                print(self.dir)
                item = 'a'
                if item in self.dir:
                    print('PISKA')
                self.dir.clear()

            else:
                self.dir.append(res)
                print(self.dir)
                print(res)
                print("время не меняется")


if __name__ == '__main__':
    win32api.LoadKeyboardLayout('00000409', 1)
    MainFunc()

#worked upper


import string
#
# #arr = ['a', 's', 'd', '1', 's', 'd', 'w', 'e', 'q']
# arr2 = ['=', 'w', 'r', 'p', 'f', ';', 'a', 'e', 'e', '[', 'w', 'q', 'r', "'", 'q', 'r', '3', 'caps lock', ';',
#         'D', 'A', 'S', 'D', 'shift', 'alt', 'ctrl', 'F', '.', 'C', 'F', 'R', 'D', 'shift', 'alt', 'D', 'shift']
# arr2_len = len(arr2)
# print(arr2_len)
#
#
#
#
# res = dict((i, arr2.count(i)) for i in arr2)
# print(len(res))
#
# print(res)



# import keyboard

#keyboard.press_and_release('shift+s, space')

#keyboard.write('The quick brown fox jumps over the lazy dog.')

#keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
#keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
#keyboard.wait('esc')

# Record events until 'esc' is pressed.
#recorded = keyboard.record(until='esc')

# Then replay back at three times the speed.
#keyboard.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
# keyboard.add_abbreviation('@@', 'vitalik.shchudlo01@ukr.net')


# Block forever, like `while True`.
# keyboard.wait()




