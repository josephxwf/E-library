# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisteredUser.ui'
#
# Created: Wed Dec  2 21:08:41 2015
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!
import pickle
from PyQt4 import QtCore, QtGui
import os
import shutil
from Book import Book
from Library import Library
from bookpageGUI import BookPageGUI

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class registeredUser(QtGui.QMainWindow):
    def __init__(self,user):
        self.library = Library()
        super(registeredUser,self).__init__()
        self.setupUi(self,user)
    def setupUi(self, MainWindow,user):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
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
        self.Name = QtGui.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(410, 30, 51, 20))
        self.Name.setObjectName(_fromUtf8("Name"))
        self.TotalPoints = QtGui.QLabel(self.centralwidget)
        self.TotalPoints.setGeometry(QtCore.QRect(410, 70, 81, 31))
        self.TotalPoints.setObjectName(_fromUtf8("TotalPoints"))
        self.NameOutput = QtGui.QLabel(self.centralwidget)
        self.NameOutput.setGeometry(QtCore.QRect(475, 22, 121, 31))
        self.NameOutput.setText(_fromUtf8(user.username))
        self.NameOutput.setObjectName(_fromUtf8("NameOutput"))
        self.PointOutput = QtGui.QLabel(self.centralwidget)
        self.PointOutput.setGeometry(QtCore.QRect(510, 70, 81, 31))
        self.PointOutput.setText(_fromUtf8(str(user.point)))
        self.PointOutput.setObjectName(_fromUtf8("PointOutput"))
        self.ContributeBooks = QtGui.QLabel(self.centralwidget)
        self.ContributeBooks.setGeometry(QtCore.QRect(470, 150, 111, 31))
        self.ContributeBooks.setObjectName(_fromUtf8("ContributeBooks"))
        self.BookTitile = QtGui.QLabel(self.centralwidget)
        self.BookTitile.setGeometry(QtCore.QRect(410, 200, 81, 31))
        self.BookTitile.setObjectName(_fromUtf8("BookTitile"))
        self.PointsRequested = QtGui.QLabel(self.centralwidget)
        self.PointsRequested.setGeometry(QtCore.QRect(410, 250, 111, 31))
        self.PointsRequested.setObjectName(_fromUtf8("PointsRequested"))
        self.BookTitileInput = QtGui.QLineEdit(self.centralwidget)
        self.BookTitileInput.setGeometry(QtCore.QRect(530, 200, 101, 21))
        self.BookTitileInput.setObjectName(_fromUtf8("BookTitileInput"))
        self.pointsInput = QtGui.QLineEdit(self.centralwidget)
        self.pointsInput.setGeometry(QtCore.QRect(530, 250, 61, 21))
        self.pointsInput.setObjectName(_fromUtf8("pointsInput"))
        self.BookSummary = QtGui.QLabel(self.centralwidget)
        self.BookSummary.setGeometry(QtCore.QRect(410, 290, 101, 31))
        self.BookSummary.setObjectName(_fromUtf8("BookSummary"))
        self.bookSummaryInput = QtGui.QTextEdit(self.centralwidget)
        self.bookSummaryInput.setGeometry(QtCore.QRect(530, 300, 211, 78))
        self.bookSummaryInput.setObjectName(_fromUtf8("bookSummaryInput"))
        self.Uploadbookbutton = QtGui.QPushButton(self.centralwidget)
        self.Uploadbookbutton.setGeometry(QtCore.QRect(410, 450, 151, 32))
        self.Uploadbookbutton.setObjectName(_fromUtf8("Uploadbookbutton"))
        self.CoverPagebutton = QtGui.QPushButton(self.centralwidget)
        self.CoverPagebutton.setGeometry(QtCore.QRect(410, 390, 110, 32))
        self.CoverPagebutton.setObjectName(_fromUtf8("CoverPagebutton"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 340, 101, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(540, 230, 241, 16))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(540, 280, 241, 16))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(550, 400, 231, 21))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 370, 256, 161))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)




        QtCore.QObject.connect(self.Uploadbookbutton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectFile)

        QtCore.QObject.connect(self.top5List, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.open_book)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_book(self, item):
        #print("open........")
        #print(str(item.text()))
        with open('book_data.pkl', 'r') as input:
            find = False
            #for line in  file_handle:
            while(not find):
                book = pickle.load(input)
                if book.title == str(item.text()):
                    print("success upload book")
                    find = True


                    self.bookitem = BookPageGUI(book)
                    self.bookitem.show()

    #def makebooksdatabase(self):
    #    os.mkdir('Database')
    #    os.mkdir('PendingBooks')

    def selectFile(self):
    #searchInput.setText(QFileDialog.getOpenFileName(self))
        summary= self.bookSummaryInput.toPlainText()   #get data from input
        title = self.BookTitileInput.text()
        points =  self.pointsInput.text()
        if not summary:
            self.label_10.setText(_fromUtf8("Summary is required!"))
            print("Summary is required")
        elif not title:
            self.label_11.setText(_fromUtf8("Title is required!"))
            print("Title is required")
        elif not points:
            self.label_12.setText(_fromUtf8("Points is required!!"))
            print("Points is required!!")
        else:
            with open('book_data.pkl', 'a') as output:
                book = Book(title, points )
                pickle.dump(book, output)
                del book
                self.close()


        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
            '/home')
        print fname
    #f = open(fname, 'r')
        #if os.path.isdir('/PendingBooks'):
        #os.mkdir('Catalog')
        #os.chmod('Catalog', 0o777)
        shutil.copy(str(fname), 'Catalog')
        #    os.mkdir('PendingBooks') #copy the path of this folder
        #    os.chmod('pendingBooks', 0777)
        #    shutil.copy(str(fname), '/PendingBooks')


    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Add Book to Catalog')
        file = open(fname, 'w')
        text = file.read()
        file.write(text)
        file.close()

    def uploadCoverPage(self): #either make a cover page directory or use 1st page of file as coverpage?
         iname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
            '/home')



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.top5List.isSortingEnabled()

        self.top5List.setSortingEnabled(False)
        books = self.library.top5Book
        for i in range(5):
            item = self.top5List.item(i)
            item.setText(QtGui.QApplication.translate("MainWindow", books[i].title, None))
        self.top5List.setSortingEnabled(__sortingEnabled)


        self.top5_label.setText(QtGui.QApplication.translate("MainWindow", "Top5", None, QtGui.QApplication.UnicodeUTF8))
        self.Name.setText(QtGui.QApplication.translate("MainWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalPoints.setText(QtGui.QApplication.translate("MainWindow", "Total Points:", None, QtGui.QApplication.UnicodeUTF8))
        self.ContributeBooks.setText(QtGui.QApplication.translate("MainWindow", "Contribute Books:", None, QtGui.QApplication.UnicodeUTF8))
        self.BookTitile.setText(QtGui.QApplication.translate("MainWindow", "Book Titile:", None, QtGui.QApplication.UnicodeUTF8))
        self.PointsRequested.setText(QtGui.QApplication.translate("MainWindow", "Points Requested:", None, QtGui.QApplication.UnicodeUTF8))
        self.BookSummary.setText(QtGui.QApplication.translate("MainWindow", "Book Summary:", None, QtGui.QApplication.UnicodeUTF8))
        self.Uploadbookbutton.setText(QtGui.QApplication.translate("MainWindow", "Upload This Book", None, QtGui.QApplication.UnicodeUTF8))
        self.CoverPagebutton.setText(QtGui.QApplication.translate("MainWindow", "CoverPage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Reading History:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
