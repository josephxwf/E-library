# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from signUp import SignUp
from bookpageGUI import BookPageGUI
from superuserGUI import SuperUserPage

import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Visitor_MainWindow(object):
    def __init__(self, library):
        self.library = library
        self.user =None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(577, 393)
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
        for i in range(5):
            item = QtGui.QListWidgetItem()
            self.top5List.addItem(item)
        self.top5_label = QtGui.QLabel(self.centralwidget)
        self.top5_label.setGeometry(QtCore.QRect(40, 80, 54, 12))
        self.top5_label.setObjectName(_fromUtf8("top5_label"))
        self.signinButton = QtGui.QPushButton(self.centralwidget)
        self.signinButton.setGeometry(QtCore.QRect(351, 121, 75, 23))
        self.signinButton.setObjectName(_fromUtf8("signinButton"))
        self.signUpButton = QtGui.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(432, 121, 75, 23))
        self.signUpButton.setObjectName(_fromUtf8("signUpButton"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 40, 203, 70))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.warning = QtGui.QLabel(self.widget)
        self.warning.setEnabled(True)
        self.warning.setText(_fromUtf8(""))
        self.warning.setObjectName(_fromUtf8("warning"))
        self.verticalLayout.addWidget(self.warning)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.userNameLaber = QtGui.QLabel(self.widget)
        self.userNameLaber.setObjectName(_fromUtf8("userNameLaber"))
        self.horizontalLayout.addWidget(self.userNameLaber)
        self.usernameInput = QtGui.QLineEdit(self.widget)
        self.usernameInput.setObjectName(_fromUtf8("usernameInput"))
        self.horizontalLayout.addWidget(self.usernameInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.passwordLabel = QtGui.QLabel(self.widget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.horizontalLayout_2.addWidget(self.passwordLabel)
        self.passwordInput = QtGui.QLineEdit(self.widget)
        self.passwordInput.setObjectName(_fromUtf8("passwordInput"))
        self.horizontalLayout_2.addWidget(self.passwordInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 23))
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

        QtCore.QObject.connect(self.signinButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.signIn)
        QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.signUp)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchBook)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def searchBook(self):
        keyWord = str(self.searchInput.text())
        result = self.library.searchBook(keyWord)
        if len(result) == 0:
            # QtGui.QMessageBox.warning(self, "Sorry", "we can't find any result.")
            print("Sorry, we can't find any result.")
        else:
            for i in range(len(result)):
                item = self.top5List.item(i)
                item.setText(_translate("MainWindow", result[i].title, None))

    def signUp(self):
        self.signUp = SignUp()
        self.signUp.show()

    def signIn(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        user = None
        if not username:
            self.warning.setText(_fromUtf8("username is required"))
            print("username is required")
        if not password:
            self.warning.setText(_fromUtf8("password is required"))
            print("password is required")
        else:
            for i in self.library.userData:
                if str(username) == i.username:
                    print("success user")
                    if str(password) == i.password:
                        print("login success")
                        user = i
                    else:
                        print("password wrong")
                    break

            if user == None:
                print("username is invalid")
            else:
                self.user = user
                if self.user.superUser == True:
                    self.UserPage = SuperUserPage(self.library, self.user)
                    self.UserPage.show()
                else:
                    pass # need register Page



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        __sortingEnabled = self.top5List.isSortingEnabled()

        self.top5List.setSortingEnabled(False)
        books = self.library.top5Book
        for i in range(5):
            item = self.top5List.item(i)
            item.setText(_translate("MainWindow", books[i].title, None))
        self.top5List.setSortingEnabled(__sortingEnabled)

        self.top5_label.setText(_translate("MainWindow", "Top5", None))
        self.signinButton.setText(_translate("MainWindow", "sign in", None))
        self.signUpButton.setText(_translate("MainWindow", "sign up", None))
        self.userNameLaber.setText(_translate("MainWindow", "User name:", None))
        self.passwordLabel.setText(_translate("MainWindow", "Password:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Visitor_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
