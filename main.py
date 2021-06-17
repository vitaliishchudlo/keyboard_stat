from PyQt5 import QtWidgets
from gui import Ui_StartWindow, Ui_LoginWindow

import sys


class StartWindow(QtWidgets.QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_login.clicked.connect(self.)


    def go_login(self):
        self.win_login = Ui_LoginWindow()
        self.win_login.show()
        self.hide()

    def go_register(self):
        pass


def run_app():
    app = QtWidgets.QApplication(sys.argv)
    wn = StartWindow()
    wn.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()

