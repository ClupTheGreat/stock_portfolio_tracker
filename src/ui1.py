# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src//ui1.ui'
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
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 140, 80, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.daily_chart = QtWidgets.QPushButton(self.layoutWidget)
        self.daily_chart.setObjectName("daily_chart")
        self.verticalLayout_2.addWidget(self.daily_chart)
        self.weekly_chart = QtWidgets.QPushButton(self.layoutWidget)
        self.weekly_chart.setObjectName("weekly_chart")
        self.verticalLayout_2.addWidget(self.weekly_chart)
        self.monthly_chart = QtWidgets.QPushButton(self.layoutWidget)
        self.monthly_chart.setObjectName("monthly_chart")
        self.verticalLayout_2.addWidget(self.monthly_chart)
        self.get_sma = QtWidgets.QPushButton(self.layoutWidget)
        self.get_sma.setObjectName("get_sma")
        self.verticalLayout_2.addWidget(self.get_sma)
        self.get_macd = QtWidgets.QPushButton(self.layoutWidget)
        self.get_macd.setObjectName("get_macd")
        self.verticalLayout_2.addWidget(self.get_macd)
        self.get_rsi = QtWidgets.QPushButton(self.layoutWidget)
        self.get_rsi.setObjectName("get_rsi")
        self.verticalLayout_2.addWidget(self.get_rsi)
        self.anal_macd = QtWidgets.QPushButton(self.layoutWidget)
        self.anal_macd.setObjectName("anal_macd")
        self.verticalLayout_2.addWidget(self.anal_macd)
        self.anal_sma = QtWidgets.QPushButton(self.layoutWidget)
        self.anal_sma.setObjectName("anal_sma")
        self.verticalLayout_2.addWidget(self.anal_sma)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 341, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(560, 130, 341, 591))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(680, 70, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 631, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.list_stock = QtWidgets.QListWidget(self.tab)
        self.list_stock.setGeometry(QtCore.QRect(50, 110, 361, 371))
        self.list_stock.setObjectName("list_stock")
        self.value_investment = QtWidgets.QLabel(self.tab)
        self.value_investment.setGeometry(QtCore.QRect(650, 30, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        self.value_investment.setFont(font)
        self.value_investment.setObjectName("value_investment")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 510, 531, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.value_investment_2 = QtWidgets.QLabel(self.tab)
        self.value_investment_2.setGeometry(QtCore.QRect(560, 530, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(20)
        self.value_investment_2.setFont(font)
        self.value_investment_2.setObjectName("value_investment_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(480, 180, 91, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_stock = QtWidgets.QPushButton(self.layoutWidget1)
        self.add_stock.setObjectName("add_stock")
        self.verticalLayout.addWidget(self.add_stock)
        self.buy_stock = QtWidgets.QPushButton(self.layoutWidget1)
        self.buy_stock.setObjectName("buy_stock")
        self.verticalLayout.addWidget(self.buy_stock)
        self.sell_stock = QtWidgets.QPushButton(self.layoutWidget1)
        self.sell_stock.setObjectName("sell_stock")
        self.verticalLayout.addWidget(self.sell_stock)
        self.tabWidget.addTab(self.tab, "")
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
        self.label_2.setText(_translate("MainWindow", "Available Stocks"))
        self.pushButton.setText(_translate("MainWindow", "BUY"))
        self.pushButton_2.setText(_translate("MainWindow", "SELL"))
        self.daily_chart.setText(_translate("MainWindow", "Daily Chart"))
        self.weekly_chart.setText(_translate("MainWindow", "Weekly Chart"))
        self.monthly_chart.setText(_translate("MainWindow", "Monthly Chart"))
        self.get_sma.setText(_translate("MainWindow", "Get SMA"))
        self.get_macd.setText(_translate("MainWindow", "Get MACD"))
        self.get_rsi.setText(_translate("MainWindow", "Get RSI"))
        self.anal_macd.setText(_translate("MainWindow", "Analyse MACD"))
        self.anal_sma.setText(_translate("MainWindow", "Analyse SMA"))
        self.label_4.setText(_translate("MainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Stock Buying / Analysis"))
        self.label.setText(_translate("MainWindow", "Your Total Investment Value: "))
        self.value_investment.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Current portfolio value: "))
        self.value_investment_2.setText(_translate("MainWindow", "TextLabel"))
        self.add_stock.setText(_translate("MainWindow", "Add"))
        self.buy_stock.setText(_translate("MainWindow", "BUY"))
        self.sell_stock.setText(_translate("MainWindow", "SELL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Portfolio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
