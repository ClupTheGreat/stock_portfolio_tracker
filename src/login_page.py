from login import Ui_loginWindow
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox


def app():
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)

    # Login button
    ui.pushButton.clicked.connect(lambda: print("hello"))

    # Register button
    ui.pushButton_2.clicked.connect(lambda: print("hello"))

    loginWindow.show()
    sys.exit(app.exec_())

app()