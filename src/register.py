# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src//register.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerWindow(object):
    def setupUi(self, registerWindow):
        registerWindow.setObjectName("registerWindow")
        registerWindow.resize(800, 363)
        self.centralwidget = QtWidgets.QWidget(registerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(270, 120, 431, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(270, 180, 431, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 110, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.finishRegistration = QtWidgets.QPushButton(self.centralwidget)
        self.finishRegistration.setGeometry(QtCore.QRect(450, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.finishRegistration.setFont(font)
        self.finishRegistration.setObjectName("finishRegistration")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(570, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 80, 241, 16))
        self.label_4.setObjectName("label_4")
        registerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(registerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        registerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(registerWindow)
        self.statusbar.setObjectName("statusbar")
        registerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(registerWindow)
        QtCore.QMetaObject.connectSlotsByName(registerWindow)

    def retranslateUi(self, registerWindow):
        _translate = QtCore.QCoreApplication.translate
        registerWindow.setWindowTitle(_translate("registerWindow", "Register"))
        self.label_3.setText(_translate("registerWindow", "Register User"))
        self.label.setText(_translate("registerWindow", "Username :"))
        self.label_2.setText(_translate("registerWindow", "Password  :"))
        self.finishRegistration.setText(_translate("registerWindow", "Register"))
        self.cancel.setText(_translate("registerWindow", "Cancel"))
        self.label_4.setText(_translate("registerWindow", "Have a 5 letter username and a 5 letter password "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerWindow = QtWidgets.QMainWindow()
    ui = Ui_registerWindow()
    ui.setupUi(registerWindow)
    registerWindow.show()
    sys.exit(app.exec_())
