# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registeredUser.ui'
#
# Created: Tue Dec  1 08:31:34 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
import os
import shutil

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

class registeredUser(QtGui.QMainWindow):
    def __init__(self,user):
        super(registeredUser,self).__init__()
        self.setupUi(self,user)
    def setupUi(self, MainWindow,user):
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
        self.passwordLabel_4 = QtGui.QLabel(self.centralwidget)
        self.passwordLabel_4.setGeometry(QtCore.QRect(320, 90, 121, 28))
        self.passwordLabel_4.setObjectName(_fromUtf8("passwordLabel_4"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 360, 256, 91))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 330, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 180, 141, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(320, 360, 231, 91))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(320, 20, 79, 32))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.userNameLaber = QtGui.QLabel(self.splitter)
        self.userNameLaber.setObjectName(_fromUtf8("userNameLaber"))
        self.passwordLabel_2 = QtGui.QLabel(self.splitter)
        self.passwordLabel_2.setObjectName(_fromUtf8("passwordLabel_2"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(320, 220, 222, 23))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(320, 260, 252, 23))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(310, 140, 308, 32))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.signUpButton = QtGui.QPushButton(self.splitter_2)
        self.signUpButton.setObjectName(_fromUtf8("signUpButton"))
        self.pushButton_2 = QtGui.QPushButton(self.splitter_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 330, 111, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
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
        QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #def makebooksdatabase(self):
        #    os.mkdir('Database')
        #    os.mkdir('PendingBooks')

    def selectFile(self):
        #searchInput.setText(QFileDialog.getOpenFileName(self))
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')
        #f = open(fname, 'r')
        if os.path.isdir('/Users/khadeeja/MyGitHub/E-library/library/PendingBooks'):
           shutil.copy(str(fname), '/Users/khadeeja/MyGitHub/E-library/library/PendingBooks')
        else:
           os.mkdir('PendingBooks') #copy the path of this folder
           shutil.copy(str(fname), '/Users/khadeeja/MyGitHub/E-library/library/PendingBooks')
        ##pushButton.clicked.connect(selectFile)

    def uploadCoverPage(self): #either make a cover page directory or use 1st page of file as coverpage?
        iname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')

    def uploadBookSummary(self):
        sname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')

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
        self.passwordLabel_4.setText(_translate("MainWindow", "Contribute books:", None))
        self.label.setText(_translate("MainWindow", "Reading history:", None))
        self.pushButton.setText(_translate("MainWindow", "Upload cover page", None))
        self.userNameLaber.setText(_translate("MainWindow", "User name:", None))
        self.passwordLabel_2.setText(_translate("MainWindow", "Total Points:", None))
        self.label_2.setText(_translate("MainWindow", "Book Title:", None))
        self.label_3.setText(_translate("MainWindow", "Reading Points:", None))
        self.signUpButton.setText(_translate("MainWindow", "Upload book", None))
        self.pushButton_2.setText(_translate("MainWindow", "Upload book summary", None))
        self.label_5.setText(_translate("MainWindow", "Pending books:", None))
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
