# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookpage.ui'
#
# Created: Thu Dec  3 13:57:42 2015
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
#import popplerqt4    fot pdf file

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class BookPageGUI(QtGui.QDialog):

    def __init__(self,book,user):
        self.user = user
        super(BookPageGUI,self).__init__()
        self.setupUi(self,book,user)
        self.book = book

    def setupUi(self, Form, book,user):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 647)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 20, 61, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.Ratelabel = QtGui.QLabel(Form)
        self.Ratelabel.setGeometry(QtCore.QRect(50, 280, 111, 31))
        self.Ratelabel.setObjectName(_fromUtf8("label_3"))

        self.readButton = QtGui.QPushButton(Form)
        self.readButton.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.readButton.setObjectName(_fromUtf8("pushButton"))

        self.closeBookButton = QtGui.QPushButton(Form)
        self.closeBookButton.setGeometry(QtCore.QRect(400, 240, 75, 23))
        self.closeBookButton.setObjectName(_fromUtf8("pushButton_3"))

        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(70, 70, 151, 191))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        # get coverage page
        self.label_9.setPixmap(QtGui.QPixmap(os.getcwd() + "/" + book.cover_page))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 520, 481, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.submitButton = QtGui.QPushButton(Form)
        self.submitButton.setGeometry(QtCore.QRect(50, 600, 75, 23))
        self.submitButton.setObjectName(_fromUtf8("pushButton_2"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 320, 481, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.commentslabel = QtGui.QLabel(self.layoutWidget)
        self.commentslabel.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.commentslabel)
        self.textBrowser_2 = QtGui.QTextBrowser(self.layoutWidget)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.booktitle = QtGui.QLabel(Form)
        self.booktitle.setGeometry(QtCore.QRect(350, 18, 170, 31))
        self.booktitle.setText(_fromUtf8(book.title))
        self.booktitle.setObjectName(_fromUtf8("label_10"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 60, 61, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.author = QtGui.QLabel(Form)
        self.author.setGeometry(QtCore.QRect(350, 60, 151, 31))
        self.author.setText(_fromUtf8(book.author))
        self.author.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 100, 61, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(270, 210, 201, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.currentUserTimelabel  = QtGui.QLabel(Form)
        self.currentUserTimelabel.setGeometry(QtCore.QRect(270, 270, 201, 31))
        self.currentUserTimelabel.setObjectName(_fromUtf8("label_5"))
        self.currentUserTime = QtGui.QLabel(Form)
        self.currentUserTime.setGeometry(QtCore.QRect(480, 270, 61, 21))
        self.currentUserTime.setText(_fromUtf8(str(user.time)))

        self.requestPoint = QtGui.QLabel(Form)
        self.requestPoint.setGeometry(QtCore.QRect(480, 215, 61, 21))
        self.requestPoint.setText(_fromUtf8(str(book.requestPoint)))

        self.requestPoint.setObjectName(_fromUtf8("label_7"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(270, 130, 291, 81))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setText(_fromUtf8(book.summary))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        QtCore.QObject.connect(self.readButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.readBook)
        QtCore.QObject.connect(self.closeBookButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeBook)

    def readBook(self):
        print(self.book.title + ".txt")
        if self.user.time > 0 :
          file = QtCore.QFile('PendingBooks/'+ self.book.title+ ".txt")
          file.open(QtCore.QIODevice.ReadOnly)
          stream = QtCore.QTextStream(file)
          self.textBrowser_2.setText(stream.readAll())
          self.time1 = QtCore.QTime.currentTime()
    def  closeBook(self):
          self.time2= QtCore.QTime.currentTime()
          self.totalTime= self.time1.secsTo(self.time2)
          self.user.time = self.user.time - self.totalTime
          print self.user.time
          print self.totalTime

        #d = popplerqt4.Poppler.Document.load('PendingBooks/'+ self.book.title+ ".txt")


    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "BookTitle:", None, QtGui.QApplication.UnicodeUTF8))
        self.Ratelabel.setText(QtGui.QApplication.translate("Form", "Rate this book", None, QtGui.QApplication.UnicodeUTF8))
        self.readButton.setText(QtGui.QApplication.translate("Form", "read", None, QtGui.QApplication.UnicodeUTF8))

        self.closeBookButton.setText(QtGui.QApplication.translate("Form", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("Form", "submit", None, QtGui.QApplication.UnicodeUTF8))
        self.commentslabel.setText(QtGui.QApplication.translate("Form", "comments", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Author:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Summary:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Points required to read this book:", None, QtGui.QApplication.UnicodeUTF8))
        self.currentUserTimelabel.setText(QtGui.QApplication.translate("Form", "Your Current Total Points:", None, QtGui.QApplication.UnicodeUTF8))

# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Form = QtGui.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
