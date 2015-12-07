# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorGUI.ui'
#
# Created: Sun Dec  6 22:45:27 2015
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.resize(917, 606)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.signinButton = QtGui.QPushButton(self.centralwidget)
        self.signinButton.setGeometry(QtCore.QRect(750, 100, 75, 23))
        self.signinButton.setObjectName(_fromUtf8("signinButton"))
        self.signUpButton = QtGui.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(750, 320, 75, 23))
        self.signUpButton.setObjectName(_fromUtf8("signUpButton"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(690, 10, 201, 82))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.warning = QtGui.QLabel(self.layoutWidget)
        self.warning.setEnabled(True)
        self.warning.setText(_fromUtf8(""))
        self.warning.setObjectName(_fromUtf8("warning"))
        self.verticalLayout.addWidget(self.warning)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.userNameLaber = QtGui.QLabel(self.layoutWidget)
        self.userNameLaber.setObjectName(_fromUtf8("userNameLaber"))
        self.horizontalLayout.addWidget(self.userNameLaber)
        self.usernameInput = QtGui.QLineEdit(self.layoutWidget)
        self.usernameInput.setObjectName(_fromUtf8("usernameInput"))
        self.horizontalLayout.addWidget(self.usernameInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.passwordLabel = QtGui.QLabel(self.layoutWidget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.horizontalLayout_2.addWidget(self.passwordLabel)
        self.passwordInput = QtGui.QLineEdit(self.layoutWidget)
        self.passwordInput.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordInput.setObjectName(_fromUtf8("passwordInput"))
##
        self.horizontalLayout_2.addWidget(self.passwordInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.EbookLibraryTitle_label = QtGui.QLabel(self.centralwidget)
        self.EbookLibraryTitle_label.setGeometry(QtCore.QRect(20, 20, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.EbookLibraryTitle_label.setFont(font)
        self.EbookLibraryTitle_label.setTextFormat(QtCore.Qt.PlainText)
        self.EbookLibraryTitle_label.setScaledContents(False)
        self.EbookLibraryTitle_label.setObjectName(_fromUtf8("EbookLibraryTitle_label"))
        self.EbookLibraryDescription_label = QtGui.QLabel(self.centralwidget)
        self.EbookLibraryDescription_label.setGeometry(QtCore.QRect(20, 60, 631, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.EbookLibraryDescription_label.setFont(font)
        self.EbookLibraryDescription_label.setObjectName(_fromUtf8("EbookLibraryDescription_label"))
        self.Createaccount_label = QtGui.QLabel(self.centralwidget)
        self.Createaccount_label.setGeometry(QtCore.QRect(720, 170, 161, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Createaccount_label.setFont(font)
        self.Createaccount_label.setObjectName(_fromUtf8("Createaccount_label"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 100, 228, 32))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.searchInput = QtGui.QLineEdit(self.splitter)
        self.searchInput.setObjectName(_fromUtf8("searchInput"))
        self.searchButton = QtGui.QPushButton(self.splitter)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(690, 200, 201, 116))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Firstname_label = QtGui.QLabel(self.layoutWidget1)
        self.Firstname_label.setObjectName(_fromUtf8("Firstname_label"))
        self.gridLayout.addWidget(self.Firstname_label, 0, 0, 1, 1)
        self.Firstname_input = QtGui.QLineEdit(self.layoutWidget1)
        self.Firstname_input.setObjectName(_fromUtf8("Firstname_input"))
        self.gridLayout.addWidget(self.Firstname_input, 0, 1, 1, 1)
        self.Lastname_label = QtGui.QLabel(self.layoutWidget1)
        self.Lastname_label.setObjectName(_fromUtf8("Lastname_label"))
        self.gridLayout.addWidget(self.Lastname_label, 1, 0, 1, 1)
        self.Lastname_input = QtGui.QLineEdit(self.layoutWidget1)
        self.Lastname_input.setObjectName(_fromUtf8("Lastname_input"))
        self.gridLayout.addWidget(self.Lastname_input, 1, 1, 1, 1)
        self.SignupUsername_label = QtGui.QLabel(self.layoutWidget1)
        self.SignupUsername_label.setObjectName(_fromUtf8("SignupUsername_label"))
        self.gridLayout.addWidget(self.SignupUsername_label, 2, 0, 1, 1)
        self.SignupUsername_input = QtGui.QLineEdit(self.layoutWidget1)
        self.SignupUsername_input.setObjectName(_fromUtf8("SignupUsername_input"))
        self.gridLayout.addWidget(self.SignupUsername_input, 2, 1, 1, 1)
        self.SignupPassword_label = QtGui.QLabel(self.layoutWidget1)
        self.SignupPassword_label.setObjectName(_fromUtf8("SignupPassword_label"))
        self.gridLayout.addWidget(self.SignupPassword_label, 3, 0, 1, 1)
        self.SignupPassword_input = QtGui.QLineEdit(self.layoutWidget1)
        self.SignupPassword_input.setObjectName(_fromUtf8("SignupPassword_input"))
        self.SignupPassword_input.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout.addWidget(self.SignupPassword_input, 3, 1, 1, 1)
        self.BookCatalog = QtGui.QListWidget(self.centralwidget)
        self.BookCatalog.setGeometry(QtCore.QRect(20, 140, 651, 421))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(13)
        self.BookCatalog.setFont(font)
        self.BookCatalog.setObjectName(_fromUtf8("BookCatalog"))
        for i in range(5):
            item = QtGui.QListWidgetItem()
            self.BookCatalog.addItem(item)
        self.verticalScrollBar = QtGui.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(660, 140, 16, 421))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.username_warning_label = QtGui.QLabel(self.centralwidget)
        self.username_warning_label.setGeometry(QtCore.QRect(690, 130, 191, 16))
        self.username_warning_label.setObjectName(_fromUtf8("username_warning_label"))
        self.password_warning_label = QtGui.QLabel(self.centralwidget)
        self.password_warning_label.setGeometry(QtCore.QRect(690, 140, 201, 16))
        self.password_warning_label.setObjectName(_fromUtf8("password_warning_label"))
        self.labelf = QtGui.QLabel(self.centralwidget)
        self.labelf.setGeometry(QtCore.QRect(690, 350, 201, 16))
        self.labelf.setObjectName(_fromUtf8("labelf"))
        self.labelL = QtGui.QLabel(self.centralwidget)
        self.labelL.setGeometry(QtCore.QRect(690, 350, 201, 16))
        self.labelL.setObjectName(_fromUtf8("labelL"))
        self.labelsu = QtGui.QLabel(self.centralwidget)
        self.labelsu.setGeometry(QtCore.QRect(690, 360, 62, 16))
        self.labelsu.setObjectName(_fromUtf8("labelsu"))
        self.labelsp = QtGui.QLabel(self.centralwidget)
        self.labelsp.setGeometry(QtCore.QRect(690, 360, 62, 16))
        self.labelsp.setObjectName(_fromUtf8("labelsp"))
##
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 22))
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
        #QtCore.QObject.connect(self.signinButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.usernameInput.selectAll)
        #QtCore.QObject.connect(self.signinButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.passwordInput.selectAll)
        #QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Firstname_input.selectAll)
        #QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Lastname_input.selectAll)
        #QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SignupUsername_input.selectAll)
        #QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SignupPassword_input.selectAll)
        QtCore.QObject.connect(self.signinButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.signIn)
        QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.signUp)

        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchBook)
        QtCore.QObject.connect(self.BookCatalog, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.open_book)
        QtCore.QObject.connect(self.verticalScrollBar, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.BookCatalog.scrollToBottom)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_book(self, item):
        book_list = self.library.loadBookData()
        if book_list:
            for book in book_list:
                if book.title == str(item.text()):
                    self.bookitem = BookPageGUI(book, None)
                    self.bookitem.show()
                    self.bookitem.closeBookButton.hide()
                    self.bookitem.rate_label.hide()
                    self.bookitem.read_button.hide()
                    self.bookitem.submit_button.hide()
                    self.bookitem.comments_label.hide()
                    self.bookitem.comments_input.hide()
                    self.bookitem.comments_text.hide()
                    break
            else:
                print("book not find")

    def searchBook(self):
        for i in range(5):
            item = self.BookCatalog.item(i)
            item.setText(_translate("MainWindow", "", None))
        keyWord = str(self.searchInput.text())
        result = self.library.searchBook(keyWord)
        if len(result) == 0:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Sorry, we can not find any result.')
        else:
            for i in range(len(result)):
                item = self.BookCatalog.item(i)
                item.setText(_translate("MainWindow", result[i].title, None))

    def signUp(self):
        self.signUp = SignUp(self.library)
        self.signUp.show()

    def signIn(self):
        inputUsername = self.usernameInput.text()
        inputPassword = self.passwordInput.text()
        user = None

        if not inputUsername:
            self.username_warning_label.setText(_fromUtf8("Username is required!"))
            print("username is required")
        elif not inputPassword:
            self.password_warning_label.setText(_fromUtf8("Password is required!"))
            print("password is required")
        else:
            self.username_warning_label.setText(_fromUtf8(""))
            self.password_warning_label.setText(_fromUtf8(""))
            user_list = self.library.loadUserData()
            for user in user_list:
                if user.username == inputUsername:
                    if user.password == inputPassword:
                        self.SuperUserPage= SuperUserPage(user, self.library)
                        self.SuperUserPage.show()
                        break
                    else:
                        self.password_warning_label.setText(_fromUtf8("Password is wrong!!"))
                        # QtGui.QMessageBox.warning(QtGui.QDialog(), 'warning', 'password is wrong!!')
            else:
                self.username_warning_label.setText(_fromUtf8("username is wrong!!"))
                # QtGui.QMessageBox.warning(QtGui.QDialog(), 'warning', 'username is wrong!!')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ebook Library", None))
        self.signinButton.setText(_translate("MainWindow", "sign in", None))
        self.signUpButton.setText(_translate("MainWindow", "sign up", None))
        self.userNameLaber.setText(_translate("MainWindow", "User name:", None))
        self.passwordLabel.setText(_translate("MainWindow", "Password:", None))
        self.EbookLibraryTitle_label.setText(_translate("MainWindow", "Ebook Library", None))
        self.EbookLibraryDescription_label.setText(_translate("MainWindow", "An Innovative Ebook Library that lets you share books and earn reading points", None))
        self.Createaccount_label.setText(_translate("MainWindow", "Create an account", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        __sortingEnabled = self.BookCatalog.isSortingEnabled()

        self.BookCatalog.setSortingEnabled(False)
        books = self.library.Catalog()
        if books:
            for i in range(len(books)):
                item = self.BookCatalog.item(i)
                item.setText(_translate("MainWindow", books[i].title, None))
        self.BookCatalog.setSortingEnabled(__sortingEnabled)

        self.Firstname_label.setText(_translate("MainWindow", "First Name:", None))
        self.Lastname_label.setText(_translate("MainWindow", "Last Name:", None))
        self.SignupUsername_label.setText(_translate("MainWindow", "User Name:", None))
        self.SignupPassword_label.setText(_translate("MainWindow", "Password:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
