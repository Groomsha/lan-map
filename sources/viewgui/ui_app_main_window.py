# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/c/Documents and Settings/icheberiak/Sources/Python/lan-map/viewgui/ui-windows/gui_app_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AppMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 700)
        MainWindow.setMinimumSize(QtCore.QSize(860, 700))
        MainWindow.setMaximumSize(QtCore.QSize(860, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 840, 590))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(31)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lan Map"))
        self.pushButton_5.setText(_translate("MainWindow", "Network Map"))
        self.pushButton_2.setText(_translate("MainWindow", "New Device"))
        self.pushButton_3.setText(_translate("MainWindow", "Edit Device"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete Device"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(27)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(28)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(29)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(30)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Device"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Interface"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IPv4 and IPv6 Address"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Subnet Mask and Link-Local"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Default Gateway"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))