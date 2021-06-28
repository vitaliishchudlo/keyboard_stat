from PyQt5 import QtWidgets
from gui import Ui_AppWindow

from threading import Thread
import sys
from win32api import LoadKeyboardLayout
import keyboard
from time import time, sleep

class AppWindow(QtWidgets.QMainWindow, Ui_AppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.th1 = Thread(target=self.keylogger) # Thread - start_keylogging
        self.th2 = Thread(target=self.send_data) # Thread - start_send_data

        self.kill_keylogger = False
        self.kill_send_info = False

        self.data = []


    def keylogger(self):
        pass

    def send_data(self):
        pass

    def run_threads(self):
        self.th1.start() # start first Thread - start_keylogging
        self.th2.start() # start second Thread - start_send_data


