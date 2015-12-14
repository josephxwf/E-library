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
from Library import Library
from Book import Book
import time

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
        """
        This function is create by PyQt4 UI code generator. But we did some change
        This function set up book page GUI.
        :param Form:
        :param book:
        :param user:
        :return:
        """
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1085, 718)
        self.book_title_label = QtGui.QLabel(Form)
        self.book_title_label.setGeometry(QtCore.QRect(270, 40, 61, 21))
        self.book_title_label.setObjectName(_fromUtf8("book_title_label"))
        self.rate_label = QtGui.QLabel(Form)
        self.rate_label.setGeometry(QtCore.QRect(50, 330, 111, 31))
        self.rate_label.setObjectName(_fromUtf8("rate_label"))

        self.read_button = QtGui.QPushButton(Form)
        self.read_button.setGeometry(QtCore.QRect(270, 330, 75, 23))
        self.read_button.setObjectName(_fromUtf8("read_button"))
        self.complaint_input = QtGui.QLineEdit(Form)
        self.complaint_input.setGeometry(QtCore.QRect(50, 660, 381, 28))
        self.complaint_input.setObjectName(_fromUtf8("complaint_input"))
        self.complaint_button = QtGui.QPushButton(Form)
        self.complaint_button.setGeometry(QtCore.QRect(450, 660, 91, 31))
        self.complaint_button.setObjectName(_fromUtf8("complaint_button"))
        self.complaint_label = QtGui.QLabel(Form)
        self.complaint_label.setGeometry(QtCore.QRect(50, 640, 111, 21))
        self.complaint_label.setObjectName(_fromUtf8("complaint_label"))
        self.closeBookButton = QtGui.QPushButton(Form)
        self.closeBookButton.setGeometry(QtCore.QRect(400, 330, 75, 23))
        self.closeBookButton.setObjectName(_fromUtf8("pushButton_3"))

        self.covepage_label = QtGui.QLabel(Form)
        self.covepage_label.setGeometry(QtCore.QRect(50, 30, 181, 261))
        self.covepage_label.setObjectName(_fromUtf8("covepage_label"))
        self.covepage_label.setPixmap(QtGui.QPixmap('CoverPage/'+ book.cover_page))
        self.covepage_label.setScaledContents(True)
        self.comments_input = QtGui.QTextEdit(Form)
        self.comments_input.setGeometry(QtCore.QRect(50, 540, 491, 61))
        self.comments_input.setObjectName(_fromUtf8("comments_input"))

        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 370, 491, 141))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.book_title_display_label = QtGui.QLabel(Form)
        self.book_title_display_label.setGeometry(QtCore.QRect(350, 40, 181, 21))
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
        self.CantComment = QtGui.QLabel(Form)
        self.CantComment.setGeometry(QtCore.QRect(400, 615, 350, 32))
        self.CantComment.setObjectName(_fromUtf8("CantComment"))

        self.review_label = QtGui.QLabel(Form)
        self.review_label.setGeometry(QtCore.QRect(50, 360, 131, 16))
        self.review_label.setObjectName(_fromUtf8("review_label"))
        self.comments_tableWidget = QtGui.QTableWidget(Form)
        self.comments_tableWidget.setGeometry(QtCore.QRect(50, 380, 491, 131))
        self.comments_tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comments_tableWidget.setFrameShape(QtGui.QFrame.Box)
        self.comments_tableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.comments_tableWidget.setRowCount(10)
        self.comments_tableWidget.setColumnCount(3)
        item = QtGui.QTableWidgetItem()
        self.comments_tableWidget.setHorizontalHeaderItem(0, item)
        item.setText("Weight")
        item = QtGui.QTableWidgetItem()
        self.comments_tableWidget.setHorizontalHeaderItem(1, item)
        item.setText("Rate")
        item = QtGui.QTableWidgetItem()
        self.comments_tableWidget.setHorizontalHeaderItem(2, item)
        item.setText("Review")
        self.comments_tableWidget.setObjectName(_fromUtf8("comments_tableWidget"))
        self.comments_tableWidget.horizontalHeader().setVisible(True)
        self.comments_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.comments_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.comments_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.write_label = QtGui.QLabel(Form)
        self.write_label.setGeometry(QtCore.QRect(50, 520, 131, 16))
        self.write_label.setObjectName(_fromUtf8("write_label"))

        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(50, 610, 325, 32))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.rate_label = QtGui.QLabel(self.splitter)
        self.rate_label.setObjectName(_fromUtf8("rate_label"))
        self.rate_lineEdit = QtGui.QLineEdit(self.splitter)
        self.rate_lineEdit.setObjectName(_fromUtf8("rate_lineEdit"))
        self.SubmitButton = QtGui.QPushButton(self.splitter)
        self.SubmitButton.setObjectName(_fromUtf8("SubmitButton"))

        self.search_button = QtGui.QPushButton(Form)
        self.search_button.setGeometry(QtCore.QRect(570, 592, 75, 23))
        self.search_button.setObjectName(_fromUtf8("read_button"))
        self.searchWordInput = QtGui.QLineEdit(Form)
        self.searchWordInput.setGeometry(QtCore.QRect(646, 592, 151, 21))
        self.searchWordInput.setObjectName(_fromUtf8("lineEdit"))

        self.invite_Input = QtGui.QLineEdit(Form)
        self.invite_Input.setGeometry(QtCore.QRect(346, 356, 100, 20))
        self.invite_Input.setObjectName(_fromUtf8("search_Input"))
        self.invite_Button = QtGui.QPushButton(Form)
        self.invite_Button.setGeometry(QtCore.QRect(270, 355, 75, 23))
        self.invite_Button.setObjectName(_fromUtf8("search_Button"))




        self.retranslateUi(Form)
        self.set_up_complaint()            # set up complaint only for user who read this book.
        QtCore.QMetaObject.connectSlotsByName(Form)
        QtCore.QObject.connect(self.read_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.readBook)
        QtCore.QObject.connect(self.closeBookButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeBook)
        QtCore.QObject.connect(self.search_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.search_and_Highlight)
        QtCore.QObject.connect(self.complaint_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.complaint)

        #QtCore.QObject.connect(self.comments_input, QtCore.SIGNAL(_fromUtf8("copyAvailable(bool)")), self.comments_text.copy)
        QtCore.QObject.connect(self.SubmitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.writecomments)
        #QtCore.QObject.connect(self.comments_input, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.comments_text.copy)
        QtCore.QObject.connect(self.invite_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.invite)



    def writecomments(self):
        library = Library()
        if str(self.book.title) in self.user.readingHistory.keys():
            comm = str(self.comments_input.toPlainText())
            rates = str(self.rate_lineEdit.text())
            self.book.comments.append(comm)
            self.book.rate.append(rates)
            if self.user.bookreadtime > 15:
                self.book.comment_type.append("Confident")
            else:
                self.book.comment_type.append("Doubdtful")
            library.update_book_data(self.book)

        else:
            self.CantComment.setText(_fromUtf8("Read the book first, then you can add a comment"))

    def set_rate_reviews_table(self):
        for index in range(len(self.book.comments)):
                item = QtGui.QTableWidgetItem()
                self.comments_tableWidget.setItem(index, 0, item)
                item.setText(_fromUtf8(self.book.comment_type[index]))
                item = QtGui.QTableWidgetItem()
                self.comments_tableWidget.setItem(index, 1, item)
                item.setText(_fromUtf8(self.book.rate[index]))
                item = QtGui.QTableWidgetItem()
                self.comments_tableWidget.setItem(index, 2, item)
                item.setText(_fromUtf8(self.book.comments[index]))



    def invite(self):
        library = Library()
        keyWord = str(self.invite_Input.text())
        user = library.searchUser(keyWord)
        print user
        if not user:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Sorry, we can not find any result.')
        else:

            if str(self.book.title) not in self.user.readingHistory.keys() and self.user.point > 0:
              self.user.point = self.user.point - int(self.book.requestPoint)



              self.user.readingHistory[str(self.book.title)] = 10
              user.inviteDic[self.user.username] = {self.book.title:False}
              # update data in database
              library.update_user_data(self.user)
              library.update_user_data(user)

            elif str(self.book.title) in self.user.readingHistory.keys() and self.user.readingHistory[str(self.book.title)] > 0:


              user.inviteDic[self.user.username] = {self.book.title:False}
              # update data in database
              library.update_user_data(user)

            elif str(self.book.title) in self.user.readingHistory.keys() and self.user.point > 0 :

              self.user.point = self.user.point - int(self.book.requestPoint)
              self.user.readingHistory[str(self.book.title)] = 10
              user.inviteDic[self.user.username] = {self.book.title:False}
              # update data in database
              library.update_user_data(self.user)
              library.update_user_data(user)

            else:
              QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Sorry, you have no points.')



    def set_up_complaint(self):
        """
        This function will check if user read this book or not.
        complaint functionality only for user who read this book.
        :return:
        """
        self.complaint_label.hide()    # first hide every things about complaint
        self.complaint_input.hide()
        self.complaint_button.hide()
        if self.user:
            reading_history = self.user.readingHistory.keys()
            for book_name in reading_history:
                if book_name == self.book.title:           # check if user read this book or not
                    self.complaint_label.show()
                    self.complaint_input.show()
                    self.complaint_button.show()


    def search_and_Highlight(self):
        # Setup the text editor
        self.text = (self.read_book_text.toPlainText()).toUtf8()

        self.searchWord = self.searchWordInput.text()

        cursor = self.read_book_text.textCursor()
        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        # Setup the regex engine
        pattern = self.searchWord
        regex = QtCore.QRegExp(pattern)
        # Process the displayed document
        pos = 0
        index = regex.indexIn(self.read_book_text.toPlainText(), pos)
        while (index != -1):
            # Select the matched text and apply the desired format
            cursor.setPosition(index)
            cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
            cursor.mergeCharFormat(format)
            # Move to the next match
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.read_book_text.toPlainText(), pos)


    def readBook(self):
        library = Library()
        users = library.loadUserData()
        self.inviter = None
        if users and self.user.inviteDic:
           for self.inviter in users:
                print "hello"
                if self.inviter.username == self.user.inviteDic.keys()[0]:
                    break
        #library = Library()
        if str(self.book.title) not in self.user.readingHistory.keys() and self.user.point > 0:
            self.user.point = self.user.point - int(self.book.requestPoint)
            self.user.bookreadtime += 5

            # update data in database
            library.update_user_data(self.user)
            self.user.readingHistory[str(self.book.title)] = 10
            library.update_user_data(self.user)
            file = QtCore.QFile('PendingBooks/'+ self.book.book_file)
            file.open(QtCore.QIODevice.ReadOnly)
            stream = QtCore.QTextStream(file)
            self.read_book_text.setText(stream.readAll())
            self.book.last_time_read = time.time()
            self.book.NumOfRead += 1
            library.update_book_data(self.book)  # update book information in database
            #d = popplerqt4.Poppler.Document.load('PendingBooks/'+ self.book.book_file)
            self.timer = QTimer(self)
            print self.timer
            self.start_time = self.user.readingHistory[str(self.book.title)]
            #self.timer.setInterval(1000)
            self.timer.start(1000)
            self.timer.timeout.connect(self.displayTime)

        elif str(self.book.title) in self.user.readingHistory.keys() and self.inviter and self.inviter.readingHistory[str(self.book.title)] > 0 and  self.user.inviteDic and self.user.inviteDic[self.user.inviteDic.keys()[0]].values()[0] is True:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Hi', 'You are using shared time reading this book!')
            print "you are using shared time reading this book"
            file = QtCore.QFile('PendingBooks/'+ self.book.book_file)
            file.open(QtCore.QIODevice.ReadOnly)
            stream = QtCore.QTextStream(file)
            self.read_book_text.setText(stream.readAll())
            self.book.last_time_read = time.time()
            self.book.NumOfRead += 1
            self.user.bookreadtime += 5
            library.update_user_data(self.user)
            library.update_book_data(self.book)
            #d = popplerqt4.Poppler.Document.load('PendingBooks/'+ self.book.book_file)
            self.timer = QTimer(self)
            print self.timer

            #library = Library()
            #users = library.loadUserData()
            #self.inviter = None
            #for self.inviter in users:
               # print "hello"
               # if self.inviter.username == self.user.inviteDic.keys()[0]:
                 # print "hello"
            if self.inviter is not None:
                  self.start_time = self.inviter.readingHistory[str(self.book.title)]
                  #self.timer.setInterval(1000)
                  self.timer.start(1000)
                  self.timer.timeout.connect(self.displayTime1)
                  self.inviter.bookreadtime += 5
                  library.update_user_data(self.inviter)
                  library.update_user_data(self.user)

        elif str(self.book.title) in self.user.readingHistory.keys() and self.user.readingHistory[str(self.book.title)] > 0:
            print self.book.requestPoint
            file = QtCore.QFile('PendingBooks/'+ self.book.book_file)
            file.open(QtCore.QIODevice.ReadOnly)
            stream = QtCore.QTextStream(file)
            self.read_book_text.setText(stream.readAll())
            self.book.last_time_read = time.time()
            self.book.NumOfRead += 1
            self.user.bookreadtime += 5
            library.update_user_data(self.user)
            library.update_book_data(self.book)
            #d = popplerqt4.Poppler.Document.load('PendingBooks/'+ self.book.book_file)
            self.timer = QTimer(self)
            print self.timer
            self.start_time = self.user.readingHistory[str(self.book.title)]
            #self.timer.setInterval(1000)
            self.timer.start(1000)
            self.timer.timeout.connect(self.displayTime)

        elif str(self.book.title) in self.user.readingHistory.keys() and self.user.point > 0 :
            print self.book.requestPoint
            self.user.point = self.user.point - int(self.book.requestPoint)
            self.user.readingHistory[str(self.book.title)] = 10
            self.user.bookreadtime += 5
            #update database
            library = Library()
            library.update_user_data(self.user)
            file = QtCore.QFile('PendingBooks/'+ self.book.book_file)
            file.open(QtCore.QIODevice.ReadOnly)
            stream = QtCore.QTextStream(file)
            self.read_book_text.setText(stream.readAll())
            self.book.last_time_read = time.time()

            library.update_book_data(self.book)
            self.timer = QTimer(self)
            #print self.timer
            self.start_time = self.user.readingHistory[str(self.book.title)]
            #self.timer.setInterval(1000)
            self.timer.start(1000)
            self.timer.timeout.connect(self.displayTime)  #call function diaplayTime continuely
        else:
            self.TimeOutMessage.setText(_fromUtf8("You have no points!"))

     # update time by 1 second
    def displayTime(self):
        self.start_time -= 1

        self.user.readingHistory[str(self.book.title)] -= 1
        if self.user.readingHistory[str(self.book.title)] < 0:
            self.user.readingHistory[str(self.book.title)] = 0

        #update database
        library = Library()
        library.update_user_data(self.user)

        if self.start_time >= 0:
           self.Timer.setText(("%d:%02d" % (self.start_time/60, self.start_time % 60)))
        else:
           self.read_book_text.setText("")
           print "Time is up!"

           self.timer.stop()

    def displayTime1(self):       # this timer is used to account shared time
        self.start_time -= 1

        self.inviter.readingHistory[str(self.book.title)] -= 1
        if self.inviter.readingHistory[str(self.book.title)] < 0:
           self.inviter.readingHistory[str(self.book.title)] = 0

        #update database
        library = Library()
        library.update_user_data(self.inviter)

        if self.start_time >= 0:
           self.Timer.setText(("%d:%02d" % (self.start_time/60, self.start_time % 60)))
        else:
           self.read_book_text.setText("")
           print "Time is up!"

           self.timer.stop()


    def closeBook(self):
        self.read_book_text.setText("")
        print "Close the book!"
        self.timer.stop()

    def complaint(self):
        """
        This function will call when user submit the complaint, it will write complaint
        reason to book object and save to book database.
        :return:
        """
        complaint_reason = str(self.complaint_input.text())
        self.book.complaint.append(complaint_reason)
        library = Library()
        library.update_book_data(self.book)
        self.complaint_button.setDisabled(True)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.book_title_label.setText(_translate("Form", "BookTitle:", None))
        self.rate_label.setText(_translate("Form", "Rate this book", None))
        self.complaint_label.setText(_translate("Form", "complaint reason:", None))
        self.read_button.setText(_translate("Form", "read", None))
        self.search_button.setText(_translate("Form", "search", None))
        self.comments_input.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Lucida Grande UI\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

        self.write_label.setText(_translate("Form", "Write a Comment:", None))
        self.review_label.setText(_translate("Form", "Reviews & Ratings", None))
        self.time_label.setText(_translate("Form", "point for 5 min", None))
        self.author_label.setText(_translate("Form", "Author:", None))
        self.set_rate_reviews_table()
        self.invite_Button.setText(_translate("superUser", "Invite", None))

        self.summary_label.setText(_translate("Form", "Summary:", None))
        self.point_label.setText(_translate("Form", "Point required:", None))
        self.point_display_label.setText(_translate("Form", str(self.book.requestPoint), None))
        self.closeBookButton.setText(QtGui.QApplication.translate("Form", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.SubmitButton.setText(_translate("Form", "Submit", None))
        self.complaint_button.setText(_translate("Form", "Submit", None))
