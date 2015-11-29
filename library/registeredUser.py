# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registeredUser.ui'
#
# Created: Sat Nov 28 14:01:06 2015
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class registeredUser(QtGui.QMainWindow):
    def __init__(self,name,points):
        super(registeredUser,self).__init__()
        self.setupUi(self,name,points)
    def setupUi(self,MainWindow,name,points):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(804, 550)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.searchInput = QtGui.QLineEdit(self.centralwidget)
        self.searchInput.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.searchInput.setObjectName(_fromUtf8("searchInput"))
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(160, 30, 75, 23))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.top5List = QtGui.QListWidget(self.centralwidget)
        self.top5List.setGeometry(QtCore.QRect(30, 110, 256, 192))
        self.top5List.setObjectName(_fromUtf8("top5List"))
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        self.top5_label = QtGui.QLabel(self.centralwidget)
        self.top5_label.setGeometry(QtCore.QRect(40, 80, 54, 12))
        self.top5_label.setObjectName(_fromUtf8("top5_label"))
        self.signUpButton = QtGui.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(460, 170, 111, 23))
        self.signUpButton.setObjectName(_fromUtf8("signUpButton"))
        self.userNameLaber = QtGui.QLabel(self.centralwidget)
        self.userNameLaber.setGeometry(QtCore.QRect(370, 60, 68, 29))
        self.userNameLaber.setObjectName(_fromUtf8("userNameLaber"))
        self.name = QtGui.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(465, 59, 161, 31))
        self.name.setText(_fromUtf8(name))
        self.name.setObjectName(_fromUtf8("name"))


        self.passwordLabel_2 = QtGui.QLabel(self.centralwidget)
        self.passwordLabel_2.setGeometry(QtCore.QRect(370, 110, 81, 28))
        self.passwordLabel_2.setObjectName(_fromUtf8("passwordLabel_2"))
        self.points = QtGui.QLabel(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(470, 110, 101, 28))
        self.points.setText(_fromUtf8(points))
        self.points.setObjectName(_fromUtf8("points"))

        self.passwordLabel_4 = QtGui.QLabel(self.centralwidget)
        self.passwordLabel_4.setGeometry(QtCore.QRect(370, 170, 91, 28))
        self.passwordLabel_4.setObjectName(_fromUtf8("passwordLabel_4"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 360, 256, 91))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(45, 323, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.top5List.isSortingEnabled()
        self.top5List.setSortingEnabled(False)
        item = self.top5List.item(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "book1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.top5List.item(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "book2", None, QtGui.QApplication.UnicodeUTF8))
        self.top5List.setSortingEnabled(__sortingEnabled)
        self.top5_label.setText(QtGui.QApplication.translate("MainWindow", "Top5", None, QtGui.QApplication.UnicodeUTF8))
        self.signUpButton.setText(QtGui.QApplication.translate("MainWindow", "Choose Files", None, QtGui.QApplication.UnicodeUTF8))
        self.userNameLaber.setText(QtGui.QApplication.translate("MainWindow", "User name:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Total Points:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel_4.setText(QtGui.QApplication.translate("MainWindow", "Upload books:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Reading history", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
