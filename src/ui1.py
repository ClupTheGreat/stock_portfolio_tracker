# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt/ui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 819)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 931, 781))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 491, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.list_stock = QtWidgets.QListWidget(self.tab)
        self.list_stock.setGeometry(QtCore.QRect(50, 110, 361, 371))
        self.list_stock.setObjectName("list_stock")
        self.value_investment = QtWidgets.QLabel(self.tab)
        self.value_investment.setGeometry(QtCore.QRect(530, 40, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        self.value_investment.setFont(font)
        self.value_investment.setObjectName("value_investment")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 510, 491, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.value_investment_2 = QtWidgets.QLabel(self.tab)
        self.value_investment_2.setGeometry(QtCore.QRect(490, 530, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        self.value_investment_2.setFont(font)
        self.value_investment_2.setObjectName("value_investment_2")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(480, 180, 91, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_stock = QtWidgets.QPushButton(self.widget)
        self.add_stock.setObjectName("add_stock")
        self.verticalLayout.addWidget(self.add_stock)
        self.buy_stock = QtWidgets.QPushButton(self.widget)
        self.buy_stock.setObjectName("buy_stock")
        self.verticalLayout.addWidget(self.buy_stock)
        self.sell_stock = QtWidgets.QPushButton(self.widget)
        self.sell_stock.setObjectName("sell_stock")
        self.verticalLayout.addWidget(self.sell_stock)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(40, 130, 341, 591))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 341, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.widget1 = QtWidgets.QWidget(self.tab_2)
        self.widget1.setGeometry(QtCore.QRect(440, 140, 77, 221))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Investment Value: "))
        self.value_investment.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Your Portfolio Value: "))
        self.value_investment_2.setText(_translate("MainWindow", "TextLabel"))
        self.add_stock.setText(_translate("MainWindow", "Add"))
        self.buy_stock.setText(_translate("MainWindow", "BUY"))
        self.sell_stock.setText(_translate("MainWindow", "SELL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_2.setText(_translate("MainWindow", "Available Stocks"))
        self.pushButton.setText(_translate("MainWindow", "BUY"))
        self.pushButton_2.setText(_translate("MainWindow", "SELL"))
        self.pushButton_3.setText(_translate("MainWindow", "ANALYSIS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
