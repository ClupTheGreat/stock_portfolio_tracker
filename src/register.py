# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src//register.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_2(object):
    def setupUi(self, register_2):
        register_2.setObjectName("register_2")
        register_2.resize(678, 273)
        self.buttonBox = QtWidgets.QDialogButtonBox(register_2)
        self.buttonBox.setGeometry(QtCore.QRect(60, 210, 591, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(register_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(220, 90, 431, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(register_2)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(register_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(220, 150, 431, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label = QtWidgets.QLabel(register_2)
        self.label.setGeometry(QtCore.QRect(50, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(register_2)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(register_2)
        self.buttonBox.accepted.connect(register_2.accept) # type: ignore
        self.buttonBox.rejected.connect(register_2.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(register_2)

    def retranslateUi(self, register_2):
        _translate = QtCore.QCoreApplication.translate
        register_2.setWindowTitle(_translate("register_2", "Register User"))
        self.label_2.setText(_translate("register_2", "Password  :"))
        self.label.setText(_translate("register_2", "Username :"))
        self.label_3.setText(_translate("register_2", "Register User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_2 = QtWidgets.QDialog()
    ui = Ui_register_2()
    ui.setupUi(register_2)
    register_2.show()
    sys.exit(app.exec_())
