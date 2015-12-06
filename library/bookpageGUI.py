# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookpage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
#import popplerqt4

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#import popplerqt4    fot pdf file


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

class BookPageGUI(QtGui.QDialog):


    def __init__(self,book,user):
        self.user = user
        self.book = book
        #self.Form = QtGui.QWidget()
        self.central = QWidget()

        super(BookPageGUI,self).__init__()
        self.setupUi(self,book,user)


    def setupUi(self, Form, book,user):
        Form.setObjectName(_fromUtf8("Form"))

        Form.resize(1065, 651)
        self.book_title_label = QtGui.QLabel(Form)
        self.book_title_label.setGeometry(QtCore.QRect(270, 30, 61, 31))
        self.book_title_label.setObjectName(_fromUtf8("book_title_label"))
        self.rate_label = QtGui.QLabel(Form)
        self.rate_label.setGeometry(QtCore.QRect(50, 330, 111, 31))
        self.rate_label.setObjectName(_fromUtf8("rate_label"))
        self.read_button = QtGui.QPushButton(Form)
        self.read_button.setGeometry(QtCore.QRect(270, 330, 75, 23))
        self.read_button.setObjectName(_fromUtf8("read_button"))

        self.closeBookButton = QtGui.QPushButton(Form)
        self.closeBookButton.setGeometry(QtCore.QRect(400, 330, 75, 23))
        self.closeBookButton.setObjectName(_fromUtf8("pushButton_3"))

        self.covepage_label = QtGui.QLabel(Form)
        self.covepage_label.setGeometry(QtCore.QRect(50, 30, 181, 261))
        self.covepage_label.setObjectName(_fromUtf8("covepage_label"))
        self.covepage_label.setPixmap(QtGui.QPixmap('CoverPage/'+ book.title+ ".jpg"))
        self.covepage_label.setScaledContents(True)
        self.comments_input = QtGui.QTextEdit(Form)
        self.comments_input.setGeometry(QtCore.QRect(50, 520, 491, 71))
        self.comments_input.setObjectName(_fromUtf8("comments_input"))
        self.submit_button = QtGui.QPushButton(Form)
        self.submit_button.setGeometry(QtCore.QRect(50, 600, 75, 23))
        self.submit_button.setObjectName(_fromUtf8("submit_button"))

        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 370, 491, 141))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.comments_label = QtGui.QLabel(self.layoutWidget)
        self.comments_label.setObjectName(_fromUtf8("comments_label"))
        self.verticalLayout_2.addWidget(self.comments_label)
        self.comments_text = QtGui.QTextBrowser(self.layoutWidget)
        self.comments_text.setObjectName(_fromUtf8("comments_text"))
        self.verticalLayout_2.addWidget(self.comments_text)
        self.book_title_display_label = QtGui.QLabel(Form)
        self.book_title_display_label.setGeometry(QtCore.QRect(350, 20, 191, 31))
        self.book_title_display_label.setText(_fromUtf8(book.title))
        self.book_title_display_label.setObjectName(_fromUtf8("book_title_display_label"))
        self.time_label = QtGui.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(410, 300, 111, 21))
        self.time_label.setObjectName(_fromUtf8("time_label"))
        self.read_book_text = QtGui.QTextBrowser(Form)
        self.read_book_text.setGeometry(QtCore.QRect(570, 40, 489, 551))
        self.read_book_text.setObjectName(_fromUtf8("read_book_text"))
        self.author_label = QtGui.QLabel(Form)
        self.author_label.setGeometry(QtCore.QRect(270, 70, 42, 16))
        self.author_label.setObjectName(_fromUtf8("author_label"))
        self.author_display_label = QtGui.QLabel(Form)
        self.author_display_label.setGeometry(QtCore.QRect(330, 70, 111, 21))
        self.author_display_label.setObjectName(_fromUtf8("author_display_label"))
        self.author_display_label.setText(_translate("Form", book.author, None))
        self.summary_label = QtGui.QLabel(Form)
        self.summary_label.setGeometry(QtCore.QRect(271, 101, 48, 16))
        self.summary_label.setObjectName(_fromUtf8("summary_label"))
        self.summary_text = QtGui.QTextBrowser(Form)
        self.summary_text.setGeometry(QtCore.QRect(271, 119, 271, 161))
        self.summary_text.setObjectName(_fromUtf8("summary_text"))
        self.summary_text.setText(_fromUtf8(book.summary))
        self.point_label = QtGui.QLabel(Form)
        self.point_label.setGeometry(QtCore.QRect(271, 301, 101, 16))
        self.point_label.setObjectName(_fromUtf8("point_label"))
        self.point_display_label = QtGui.QLabel(Form)
        self.point_display_label.setGeometry(QtCore.QRect(380, 300, 21, 21))
        self.point_display_label.setObjectName(_fromUtf8(str(book.requestPoint)))
        self.Timer = QtGui.QTextBrowser(Form)
        self.Timer.setGeometry(QtCore.QRect(570, 20, 100, 20))
        self.Timer.setObjectName(_fromUtf8("timer"))
        self.TimeOutMessage = QtGui.QLabel(Form)
        self.TimeOutMessage.setGeometry(QtCore.QRect(670, 20, 200, 20))
        self.TimeOutMessage.setObjectName(_fromUtf8("TimeOutMessage"))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        QtCore.QObject.connect(self.read_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.readBook)
        QtCore.QObject.connect(self.closeBookButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeBook)

    def readBook(self):
        print(self.book.book_file)
        if self.user.timelist[self.book.title] > 0:
            file = QtCore.QFile('PendingBooks/'+ self.book.book_file)
            file.open(QtCore.QIODevice.ReadOnly)
            stream = QtCore.QTextStream(file)
            self.read_book_text.setText(stream.readAll())

            self.timer = QTimer(self)
            print self.timer
            self.start_time = self.user.timelist[self.book.title]
            #self.timer.setInterval(1000)
            self.timer.start(1000)
            self.timer.timeout.connect(self.displayTime)


        elif self.user.point > 0 :

            self.user.point = self.user.point - self.book.requestPoint
            self.user.timelist[self.book.title] = 10
            file = QtCore.QFile('PendingBooks/'+ self.book.book_file)
            file.open(QtCore.QIODevice.ReadOnly)
            stream = QtCore.QTextStream(file)
            self.read_book_text.setText(stream.readAll())

            self.timer = QTimer(self)
            #print self.timer
            self.start_time = self.user.timelist[self.book.title]
            #self.timer.setInterval(1000)
            self.timer.start(1000)
            self.timer.timeout.connect(self.displayTime)
        else:
            self.TimeOutMessage.setText(_fromUtf8("You have no points!"))


    def displayTime(self):
        self.start_time -= 1
        self.user.timelist[self.book.title] -=1
        print self.user.timelist[self.book.title]
        if self.start_time >= 0:
           self.Timer.setText(("%d:%02d" % (self.start_time/60,self.start_time % 60)))
        else:
           self.read_book_text.setText("")
           print "Time is up!"

           self.timer.stop()


    def closeBook(self):
        self.read_book_text.setText("")
        print "Close the book!"
        self.timer.stop()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.book_title_label.setText(_translate("Form", "BookTitle:", None))
        self.rate_label.setText(_translate("Form", "Rate this book", None))
        self.read_button.setText(_translate("Form", "read", None))
        self.submit_button.setText(_translate("Form", "submit", None))
        self.comments_label.setText(_translate("Form", "comments", None))
        self.time_label.setText(_translate("Form", "point for 5 min", None))
        self.author_label.setText(_translate("Form", "Author:", None))

        self.summary_label.setText(_translate("Form", "Summary:", None))
        self.point_label.setText(_translate("Form", "Point required:", None))
        self.point_display_label.setText(_translate("Form", "50", None))
        self.closeBookButton.setText(QtGui.QApplication.translate("Form", "close", None, QtGui.QApplication.UnicodeUTF8))


#
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Form = QtGui.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
