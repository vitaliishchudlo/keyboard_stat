from PyQt5 import QtWidgets
from gui import Ui_LoginWindow
from app import AppWindow
import start


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # buttons
        self.btn_back.clicked.connect(self.go_back)
        self.btn_login.clicked.connect(self.go_app)


    def go_app(self):
        self.go_app_win = AppWindow()
        self.go_app_win.show()
        self.hide()


    def go_back(self):
        # initialization of switchable windows
        self.go_start_win = start.StartWindow()
        self.go_start_win.show()
        self.hide()
