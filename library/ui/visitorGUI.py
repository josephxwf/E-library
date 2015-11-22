# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
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
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        self.top5_label = QtGui.QLabel(self.centralwidget)
        self.top5_label.setGeometry(QtCore.QRect(40, 80, 54, 12))
        self.top5_label.setObjectName(_fromUtf8("top5_label"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 60, 203, 52))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.horizontalLayout = QtGui.QHBoxLayout()

        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.warmingLabel = QtGui.QLabel(self.layoutWidget)
        self.warmingLabel.setObjectName(_fromUtf8("warmingLabel"))
        self.horizontalLayout_3.addWidget(self.warmingLabel)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

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
        self.passwordInput.setObjectName(_fromUtf8("passwordInput"))
        self.horizontalLayout_2.addWidget(self.passwordInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.signinButton = QtGui.QPushButton(self.centralwidget)
        self.signinButton.setGeometry(QtCore.QRect(351, 131, 71, 31))
        self.signinButton.setObjectName(_fromUtf8("signinButton"))
        self.signUpButton = QtGui.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(432, 131, 71, 31))
        self.signUpButton.setObjectName(_fromUtf8("signUpButton"))
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
        QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.passwordInput.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def signIn(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if not username:
            self.warmingLabel.setInputContext("username is required")
            print("username is required")
        if not password:
            print("password is required")
        else:
            print("success")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        __sortingEnabled = self.top5List.isSortingEnabled()
        self.top5List.setSortingEnabled(False)
        item = self.top5List.item(0)
        item.setText(_translate("MainWindow", "book1", None))
        item = self.top5List.item(1)
        item.setText(_translate("MainWindow", "book2", None))
        self.top5List.setSortingEnabled(__sortingEnabled)
        self.top5_label.setText(_translate("MainWindow", "Top5", None))
        self.warmingLabel.setText(_translate("MainWindow", "warming", None))
        self.userNameLaber.setText(_translate("MainWindow", "User name:", None))
        self.passwordLabel.setText(_translate("MainWindow", "Password:", None))
        self.signinButton.setText(_translate("MainWindow", "sign in", None))
        self.signUpButton.setText(_translate("MainWindow", "sign up", None))
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

