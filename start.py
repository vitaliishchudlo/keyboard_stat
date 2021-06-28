import sys

from PyQt5 import QtWidgets

from account_management import login, register
from gui import Ui_StartWindow


class StartWindow(QtWidgets.QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.go_reg_win = register.RegisterWindow()
        self.go_log_win = login.LoginWindow()

        self.btn_login.clicked.connect(self.go_login)
        self.btn_register.clicked.connect(self.go_register)

    def go_login(self):
        self.go_log_win.show()
        self.hide()

    def go_register(self):
        self.go_reg_win.show()
        self.hide()


def run_app():
    app = QtWidgets.QApplication(sys.argv)
    wn = StartWindow()
    wn.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
