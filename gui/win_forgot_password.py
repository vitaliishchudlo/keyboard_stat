# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgot_password.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Forgot_Pass_Window(object):
    def setupUi(self, Forgot_Pass_Window):
        Forgot_Pass_Window.setObjectName("Forgot_Pass_Window")
        Forgot_Pass_Window.resize(500, 656)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Forgot_Pass_Window.sizePolicy().hasHeightForWidth())
        Forgot_Pass_Window.setSizePolicy(sizePolicy)
        Forgot_Pass_Window.setMinimumSize(QtCore.QSize(350, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Photos/Pictures/Icons/Lumicons ico pack/System/Device Keyboard.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Forgot_Pass_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Forgot_Pass_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setStyleSheet("color: blue;\n"
"outline: none;\n"
"border: 0;\n"
"background: transparent;\n"
"text-decoration: underline;")
        self.btn_back.setObjectName("btn_back")
        self.verticalLayout_2.addWidget(self.btn_back, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.text_error = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_error.sizePolicy().hasHeightForWidth())
        self.text_error.setSizePolicy(sizePolicy)
        self.text_error.setMinimumSize(QtCore.QSize(0, 50))
        self.text_error.setText("")
        self.text_error.setAlignment(QtCore.Qt.AlignCenter)
        self.text_error.setObjectName("text_error")
        self.verticalLayout_2.addWidget(self.text_error)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.login_new_pass = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_new_pass.sizePolicy().hasHeightForWidth())
        self.login_new_pass.setSizePolicy(sizePolicy)
        self.login_new_pass.setMinimumSize(QtCore.QSize(0, 30))
        self.login_new_pass.setMaximumSize(QtCore.QSize(300, 16777215))
        self.login_new_pass.setObjectName("login_new_pass")
        self.gridLayout.addWidget(self.login_new_pass, 5, 1, 1, 1)
        self.text_new_pass = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_new_pass.sizePolicy().hasHeightForWidth())
        self.text_new_pass.setSizePolicy(sizePolicy)
        self.text_new_pass.setMinimumSize(QtCore.QSize(0, 50))
        self.text_new_pass.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.text_new_pass.setObjectName("text_new_pass")
        self.gridLayout.addWidget(self.text_new_pass, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.text_login = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_login.sizePolicy().hasHeightForWidth())
        self.text_login.setSizePolicy(sizePolicy)
        self.text_login.setMinimumSize(QtCore.QSize(0, 50))
        self.text_login.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.text_login.setObjectName("text_login")
        self.gridLayout.addWidget(self.text_login, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_button = QtWidgets.QPushButton(self.centralwidget)
        self.btn_button.setObjectName("btn_button")
        self.horizontalLayout_2.addWidget(self.btn_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.line_recovery_code = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_recovery_code.sizePolicy().hasHeightForWidth())
        self.line_recovery_code.setSizePolicy(sizePolicy)
        self.line_recovery_code.setMinimumSize(QtCore.QSize(0, 30))
        self.line_recovery_code.setMaximumSize(QtCore.QSize(300, 16777215))
        self.line_recovery_code.setObjectName("line_recovery_code")
        self.gridLayout.addWidget(self.line_recovery_code, 3, 1, 1, 1)
        self.line_login = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_login.sizePolicy().hasHeightForWidth())
        self.line_login.setSizePolicy(sizePolicy)
        self.line_login.setMinimumSize(QtCore.QSize(0, 30))
        self.line_login.setMaximumSize(QtCore.QSize(300, 16777215))
        self.line_login.setObjectName("line_login")
        self.gridLayout.addWidget(self.line_login, 1, 1, 1, 1)
        self.text_recovery_code = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_recovery_code.sizePolicy().hasHeightForWidth())
        self.text_recovery_code.setSizePolicy(sizePolicy)
        self.text_recovery_code.setMinimumSize(QtCore.QSize(0, 50))
        self.text_recovery_code.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";\n"
"color: rgb(255, 0, 0);")
        self.text_recovery_code.setObjectName("text_recovery_code")
        self.gridLayout.addWidget(self.text_recovery_code, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_version = QtWidgets.QLabel(self.centralwidget)
        self.text_version.setObjectName("text_version")
        self.horizontalLayout.addWidget(self.text_version)
        self.text_FAQ = QtWidgets.QLabel(self.centralwidget)
        self.text_FAQ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_FAQ.setOpenExternalLinks(True)
        self.text_FAQ.setObjectName("text_FAQ")
        self.horizontalLayout.addWidget(self.text_FAQ)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        Forgot_Pass_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Forgot_Pass_Window)
        QtCore.QMetaObject.connectSlotsByName(Forgot_Pass_Window)

    def retranslateUi(self, Forgot_Pass_Window):
        _translate = QtCore.QCoreApplication.translate
        Forgot_Pass_Window.setWindowTitle(_translate("Forgot_Pass_Window", "NAZVA"))
        self.btn_back.setText(_translate("Forgot_Pass_Window", "❮ back"))
        self.text_new_pass.setText(_translate("Forgot_Pass_Window", "New password:"))
        self.text_login.setText(_translate("Forgot_Pass_Window", "Login: "))
        self.btn_button.setText(_translate("Forgot_Pass_Window", "Send recovery key"))
        self.text_recovery_code.setText(_translate("Forgot_Pass_Window", "RECOVERY CODE:"))
        self.text_version.setText(_translate("Forgot_Pass_Window", "version 1.5.0"))
        self.text_FAQ.setText(_translate("Forgot_Pass_Window", "<html><head/><body><p><a href=\"http://www.qtcentre.org\"><span style=\" text-decoration: underline; color:#0000ff;\">F.A.Q.</span></a></p></body></html>"))
