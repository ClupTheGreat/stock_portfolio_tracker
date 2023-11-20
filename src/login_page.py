from login import Ui_loginWindow
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from usersystem import login
from register_page import register_page_call
from uipyqt import windowManager

def show_info_messagebox(): 
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Information) 
    msg.setText("Wrong Username or Password") 
    msg.setWindowTitle("Login") 
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
    retval = msg.exec_() 

def login_check(username, password):
    res = login(username,password)
    if res[0] == True:
        return True
    else:
        show_info_messagebox()
        return False


def login_page_call():
    def login_check(username, password):
        res = login(username,password)
        if res[0] == True:
            loginWindow.hide()
            application.show()
            application.set_username(username)
            
            # appMain(res[1])
        else:
            show_info_messagebox()
            return False
        
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    
    ui = Ui_loginWindow()
    application = windowManager()
    ui.setupUi(loginWindow)

    # Login button
    ui.pushButton.clicked.connect(lambda: login_check(ui.plainTextEdit.toPlainText(), ui.plainTextEdit_2.toPlainText()))

    # Register button
    ui.pushButton_2.clicked.connect(lambda: register_page_call())
    
    loginWindow.show()
    sys.exit(app.exec_())

# login_page_call()