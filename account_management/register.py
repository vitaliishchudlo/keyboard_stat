from PyQt5 import QtWidgets
from gui import Ui_RegisterWindow
import start


class RegisterWindow(QtWidgets.QMainWindow, Ui_RegisterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.btn_back.clicked.connect(self.go_back)

    def go_back(self):
        self.go_start_win = start.StartWindow()
        self.go_start_win.show()
        self.hide()




