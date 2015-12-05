# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from User import User
import pickle
from PyQt4 import QtCore, QtGui
from signUp import SignUp
from registeredUser import registeredUser
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
        self.signinButton.setGeometry(QtCore.QRect(350, 170, 75, 23))
        self.signinButton.setObjectName(_fromUtf8("signinButton"))
        self.signUpButton = QtGui.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(440, 170, 75, 23))
        self.signUpButton.setObjectName(_fromUtf8("signUpButton"))
        self.userNameLaber = QtGui.QLabel(self.centralwidget)
        self.userNameLaber.setGeometry(QtCore.QRect(310, 50, 68, 29))
        self.userNameLaber.setObjectName(_fromUtf8("userNameLaber"))
        self.usernameInput = QtGui.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(390, 50, 151, 21))
        self.usernameInput.setObjectName(_fromUtf8("usernameInput"))
        self.passwordLabel = QtGui.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(310, 100, 61, 28))
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.passwordInput = QtGui.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(390, 100, 151, 21))
        self.passwordInput.setEchoMode(QtGui.QLineEdit.Password)

        self.passwordInput.setObjectName(_fromUtf8("passwordInput"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 70, 151, 20))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 130, 151, 20))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 231, 20))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 22))
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


        print QtCore.QTimer()
        self.retranslateUi(MainWindow)



        QtCore.QObject.connect(self.signinButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.signIn)
        QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.signUp)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchBook)
        QtCore.QObject.connect(self.top5List, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.open_book)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_book(self, item):
        with open('book_data.pkl', 'r') as input:
            find = False
            #for line in  file_handle:
            while(not find):
                book = pickle.load(input)
                if book.title == str(item.text()):
                    print("successfully open book")
                    find = True


                    self.bookitem = BookPageGUI(book,None)
                    self.bookitem.show()

                    self.bookitem.rate_label.hide()
                    self.bookitem.read_button.hide()
                    self.bookitem.submit_button.hide()
                    self.bookitem.comments_label.hide()
                    self.bookitem.comments_input.hide()
                    self.bookitem.comments_text.hide()




    def searchBook(self):
        for i in range(5):
            item = self.top5List.item(i)
            item.setText(_translate("MainWindow", "", None))
        keyWord = str(self.searchInput.text())
        result = self.library.searchBook(keyWord)
        if len(result) == 0:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Sorry, we can not find any result.')
        else:
            for i in range(len(result)):
                item = self.top5List.item(i)
                item.setText(_translate("MainWindow", result[i].title, None))

    def signUp(self):
        self.signUp = SignUp(self.library)
        self.signUp.show()

    def signIn(self):
        inputUsername = self.usernameInput.text()
        inputPassword = self.passwordInput.text()
        user = None

        if not inputUsername:
            self.label.setText(_fromUtf8("Username is required!"))
            print("username is required")
        if not inputPassword:
            self.label_2.setText(_fromUtf8("Password is required!"))
            print("password is required")
        else:
            self.label.setText(_fromUtf8(""))
            self.label_2.setText(_fromUtf8(""))
            with open('user_data.pkl', 'r') as input:
                find = False
                #for line in  file_handle:
                while(not find):
                    print("aaaa")
                    user = pickle.load(input)
                    if user.username == inputUsername and user.password == inputPassword:
                        print("success user")
                        find = True
                        if user.superUser == True:
                            self.SuperUserPage= SuperUserPage(user, self.library)
                            self.SuperUserPage.show()
                        else:
                            self.registeredUser= registeredUser(user, self.library)
                            self.registeredUser.show()

                        self.label_3.setText(_fromUtf8(""))

                if find == False:
                  self.label_3.setText(_fromUtf8("Username or Password is incorrect!"))
                  print("username or password is incorrect")


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.top5List.isSortingEnabled()

        self.top5List.setSortingEnabled(False)
        books = self.library.top5Book
        for i in range(5):
            item = self.top5List.item(i)
            item.setText(_translate("MainWindow", books[i].title, None))
        self.top5List.setSortingEnabled(__sortingEnabled)


        self.top5_label.setText(QtGui.QApplication.translate("MainWindow", "Top5", None, QtGui.QApplication.UnicodeUTF8))
        self.signinButton.setText(QtGui.QApplication.translate("MainWindow", "sign in", None, QtGui.QApplication.UnicodeUTF8))
        self.signUpButton.setText(QtGui.QApplication.translate("MainWindow", "sign up", None, QtGui.QApplication.UnicodeUTF8))
        self.userNameLaber.setText(QtGui.QApplication.translate("MainWindow", "User name:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("MainWindow", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Visitor_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
