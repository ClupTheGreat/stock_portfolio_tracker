from register import Ui_registerWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from usersystem import register
import sys
import re

def is_valid_username(username):
    pattern = r'^.{5,}$'
    return re.match(pattern, username) is not None

def is_valid_password(password):
    pattern = r'^.{5,}$'
    return re.match(pattern, password) is not None


def show_info_messagebox(message): 
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Information) 
    msg.setText(message) 
    msg.setWindowTitle("Register") 
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
    retval = msg.exec_()


def register_page_call():
    def register_account(username, password):
        if is_valid_username(username):
            if is_valid_password(password):
                res = register(username,password)
                if res == True:
                    show_info_messagebox("Registration successful, login with your username and password")
                    registerWindow.hide()
                    return True
                else:
                    show_info_messagebox("Username not available, Try Again!")
                    return False
            else:
                show_info_messagebox("Wrong password length")
        else:
            show_info_messagebox("Wrong username length")
    # app = QtWidgets.QApplication(sys.argv)
    registerWindow = QtWidgets.QMainWindow()
    ui = Ui_registerWindow()
    ui.setupUi(registerWindow)
    ui.finishRegistration.clicked.connect(lambda: register_account(ui.plainTextEdit.toPlainText(), ui.plainTextEdit_2.toPlainText()))
    ui.cancel.clicked.connect(lambda: registerWindow.close())
    registerWindow.show()
    # sys.exit(app.exec_())

# register_page_call()