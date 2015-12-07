# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperUserGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import shutil
from bookpageGUI import BookPageGUI
from Book import Book
import os
import pickle

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


class SuperUserPage(QtGui.QWidget):
    def __init__(self, user, library):
        self.user = user
        self.library = library
        self.upload_book = Book("","",0)
        self.upload_book.contribute_by = self.user
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, superUser):
        superUser.setObjectName(_fromUtf8("superUser"))
        superUser.resize(850, 615)
        self.search_Input = QtGui.QLineEdit(superUser)
        self.search_Input.setGeometry(QtCore.QRect(31, 32, 133, 20))
        self.search_Input.setObjectName(_fromUtf8("search_Input"))
        self.search_Button = QtGui.QPushButton(superUser)
        self.search_Button.setGeometry(QtCore.QRect(170, 31, 75, 23))
        self.search_Button.setObjectName(_fromUtf8("search_Button"))
        self.contributLabel = QtGui.QLabel(superUser)
        self.contributLabel.setGeometry(QtCore.QRect(450, 130, 111, 21))
        self.contributLabel.setObjectName(_fromUtf8("contributLabel"))
        self.book_title_label = QtGui.QLabel(superUser)
        self.book_title_label.setGeometry(QtCore.QRect(360, 170, 71, 21))
        self.book_title_label.setObjectName(_fromUtf8("book_title_label"))
        self.point_requested_label = QtGui.QLabel(superUser)
        self.point_requested_label.setGeometry(QtCore.QRect(360, 200, 101, 31))
        self.point_requested_label.setObjectName(_fromUtf8("point_requested_label"))
        self.book_summary_label = QtGui.QLabel(superUser)
        self.book_summary_label.setGeometry(QtCore.QRect(360, 250, 91, 16))
        self.book_summary_label.setObjectName(_fromUtf8("book_summary_label"))
        self.book_title_input = QtGui.QLineEdit(superUser)
        self.book_title_input.setGeometry(QtCore.QRect(480, 170, 113, 20))
        self.book_title_input.setObjectName(_fromUtf8("book_title_input"))
        self.point_requested_input = QtGui.QLineEdit(superUser)
        self.point_requested_input.setGeometry(QtCore.QRect(480, 210, 113, 20))
        self.point_requested_input.setObjectName(_fromUtf8("point_requested_input"))
        self.book_summary_input = QtGui.QTextEdit(superUser)
        self.book_summary_input.setGeometry(QtCore.QRect(480, 250, 201, 61))
        self.book_summary_input.setObjectName(_fromUtf8("book_summary_input"))
        self.coverpage_button = QtGui.QPushButton(superUser)
        self.coverpage_button.setGeometry(QtCore.QRect(360, 330, 101, 41))
        self.coverpage_button.setObjectName(_fromUtf8("coverpage_button"))
        self.upload_book_button = QtGui.QPushButton(superUser)
        self.upload_book_button.setGeometry(QtCore.QRect(500, 330, 101, 41))
        self.upload_book_button.setObjectName(_fromUtf8("upload_book_button"))
        self.submit_button = QtGui.QPushButton(superUser)
        self.submit_button.setGeometry(QtCore.QRect(630, 330, 111, 41))
        self.submit_button.setObjectName(_fromUtf8("submit_button"))
        self.request_Table = QtGui.QTableWidget(superUser)
        self.request_Table.setGeometry(QtCore.QRect(360, 430, 441, 161))
        self.request_Table.setObjectName(_fromUtf8("request_Table"))
        self.request_Table.setColumnCount(3)
        self.request_Table.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.request_Table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.request_Table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.request_Table.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.request_Table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.request_Table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.request_Table.setHorizontalHeaderItem(2, item)
        self.request_List_Label = QtGui.QLabel(superUser)
        self.request_List_Label.setGeometry(QtCore.QRect(360, 400, 211, 16))
        self.request_List_Label.setObjectName(_fromUtf8("request_List_Label"))
        if self.user.superUser == True:

            self.decide_button = QtGui.QPushButton(superUser)
            self.decide_button.setGeometry(QtCore.QRect(700, 450, 71, 31))
            self.decide_button.setObjectName(_fromUtf8("decide_button"))
        if self.user.superUser == False:
            self.approve_button = QtGui.QPushButton(superUser)
            self.approve_button.setGeometry(QtCore.QRect(700, 450, 71, 31))
            self.approve_button.setObjectName(_fromUtf8("approve_button"))
            self.denied_button = QtGui.QPushButton(superUser)
            self.denied_button.setGeometry(QtCore.QRect(700, 500, 71, 31))
            self.denied_button.setObjectName(_fromUtf8("denied_button"))

        self.point_Label = QtGui.QLabel(superUser)
        self.point_Label.setGeometry(QtCore.QRect(360, 90, 78, 16))
        self.point_Label.setObjectName(_fromUtf8("point_Label"))
        self.points_number_Label = QtGui.QLabel(superUser)
        self.points_number_Label.setGeometry(QtCore.QRect(470, 90, 61, 21))
        self.points_number_Label.setObjectName(_fromUtf8("points_number_Label"))
        self.username_Label = QtGui.QLabel(superUser)
        self.username_Label.setGeometry(QtCore.QRect(360, 50, 30, 16))
        self.username_Label.setObjectName(_fromUtf8("username_Label"))
        self.name_In_Label = QtGui.QLabel(superUser)
        self.name_In_Label.setGeometry(QtCore.QRect(410, 50, 100, 21))
        self.name_In_Label.setObjectName(_fromUtf8("name_In_Label"))

        self.top5_Label = QtGui.QLabel(superUser)
        self.top5_Label.setGeometry(QtCore.QRect(30, 90, 72, 16))
        self.top5_Label.setObjectName(_fromUtf8("top5_Label"))
        self.top5_List = QtGui.QListWidget(superUser)
        self.top5_List.setGeometry(QtCore.QRect(30, 130, 209, 163))
        self.top5_List.setObjectName(_fromUtf8("top5_List"))
        for i in range(5):
            item = QtGui.QListWidgetItem()
            self.top5_List.addItem(item)
        self.history_Label = QtGui.QLabel(superUser)
        self.history_Label.setGeometry(QtCore.QRect(30, 340, 96, 16))
        self.history_Label.setObjectName(_fromUtf8("history_Label"))
        self.history_List = QtGui.QListWidget(superUser)
        self.history_List.setGeometry(QtCore.QRect(30, 370, 209, 164))
        self.history_List.setObjectName(_fromUtf8("history_List"))
        item = QtGui.QListWidgetItem()
        self.history_List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.history_List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.history_List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.history_List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.history_List.addItem(item)

        self.retranslateUi(superUser)

        QtCore.QObject.connect(self.search_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchBook)
        QtCore.QObject.connect(self.top5_List, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.open_book)
        QtCore.QObject.connect(self.upload_book_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectFile)
        QtCore.QObject.connect(self.coverpage_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectCoverPage)
        QtCore.QObject.connect(self.submit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.submit)
        if self.user.superUser is True:
            QtCore.QObject.connect(self.decide_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.decide)
        else:
            QtCore.QObject.connect(self.approve_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.approve)
            QtCore.QObject.connect(self.denied_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.denied)

        QtCore.QMetaObject.connectSlotsByName(superUser)

    def approve(self):
        if self.decide_book is not None:
            self.library.update_book_data(self.decide_book, "pending_book_data.pkl", delete=True)
            self.library.update_book_data(self.decide_book)
            self.user.point += self.decide_book.superuser_set_point
            self.points_number_Label.setText(_translate("superUser", str(self.user.point), None))

            self.user.own_book.append(self.upload_book)
            self.library.update_user_data(self.user)

            self.set_pending_book_table_for_register()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'not book need approve!')

    def denied(self):
        if self.decide_book is not None:
            self.library.update_book_data(self.decide_book, "pending_book_data.pkl", delete=True)
            self.set_pending_book_table_for_register()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'not book need denied!')

    def decide(self):
        if self.decide_book is not None:
            item = self.request_Table.item(0, 2)
            point = int(item.text())             # superuser input point
            print(point)
            print(type(point))

            self.decide_book.superuser_set_point = point
            # self.library.update_book_data(self.decide_book, "pending_book_data.pkl", delete=True)
            self.library.update_book_data(self.decide_book, "pending_book_data.pkl")

            self.set_pending_book_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'not book need decide!')

    def set_pending_book_table(self):
        for index in range(3):
            item = QtGui.QTableWidgetItem()
            self.request_Table.setItem(index, 0, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table.setItem(index, 1, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table.setItem(index, 2, item)
            item = self.request_Table.item(index, 0)
            item.setText(_translate("superUser", "", None))
            item = self.request_Table.item(index, 1)
            item.setText(_translate("superUser", "", None))
            item = self.request_Table.item(index, 2)
            item.setText(_translate("superUser", "", None))
        self.decide_book = None
        pending_book = self.library.loadBookData("pending_book_data.pkl")
        if pending_book:
            index = 0
            for book in pending_book:
                if book.superuser_set_point == 0:   # check if super user didn't set point
                    if index == 0:
                        self.decide_book = book
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 0, item)
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 1, item)
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 2, item)
                    item = self.request_Table.item(index, 0)
                    item.setText(_translate("superUser", book.contribute_by, None))
                    item = self.request_Table.item(index, 1)
                    item.setText(_translate("superUser", book.title, None))
                    item = self.request_Table.item(index, 2)
                    item.setText(_translate("superUser", str(book.requestPoint), None))
                    print(index)
                    if index >= 2:
                        break
                    else:
                        index += 1


    def set_pending_book_table_for_register(self):
        for index in range(3):
            item = QtGui.QTableWidgetItem()
            self.request_Table.setItem(index, 0, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table.setItem(index, 1, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table.setItem(index, 2, item)
            item = self.request_Table.item(index, 0)
            item.setText(_translate("superUser", "", None))
            item = self.request_Table.item(index, 1)
            item.setText(_translate("superUser", "", None))
            item = self.request_Table.item(index, 2)
            item.setText(_translate("superUser", "", None))
        self.decide_book = None
        pending_book = self.library.loadBookData("pending_book_data.pkl")
        if pending_book:
            index = 0
            for book in pending_book:
                if book.superuser_set_point != 0 and book.contribute_by == self.user.username:        # check if super user set point
                    if index == 0:
                        self.decide_book = book
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 0, item)
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 1, item)
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 2, item)
                    item = self.request_Table.item(index, 0)
                    item.setText(_translate("superUser", book.title, None))
                    item = self.request_Table.item(index, 1)
                    item.setText(_translate("superUser", str(book.requestPoint), None))
                    item = self.request_Table.item(index, 2)
                    item.setText(_translate("superUser", str(book.superuser_set_point), None))
                    print(index)
                    if index == 2:
                        break
                    else:
                        index += 1


    def open_book(self, item):
        book_list = self.library.loadBookData()
        for book in book_list:
            if book.title == str(item.text()):
                self.bookitem = BookPageGUI(book, self.user)
                self.bookitem.show()
                break
        else:
            print("book not find")


    def selectFile(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if file_name:
            file_name_cut_list = str(file_name).split('/')
            print(file_name_cut_list)
            # if not self.upload_book.book_file:
            print file_name
            shutil.copy(str(file_name), 'PendingBooks')
            self.upload_book.book_file = file_name_cut_list[-1]
            print(self.upload_book.book_file)
            self.upload_book_button.setDisabled(True)
            # else:
            #     # path = os.getcwd()+"/PendingBooks"
            #     print(self.upload_book.book_file)
            #     os.remove(self.upload_book.book_file)
            #     shutil.copy(str(file_name), 'PendingBooks')
            #     self.upload_book.book_file = file_name_cut_list[-1]


    def selectCoverPage(self):
        image = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if image:
            file_name_cut_list = str(image).split('/')
            shutil.copy(str(image), 'CoverPage')
            self.upload_book.cover_page = file_name_cut_list[-1]
            print(self.upload_book.cover_page)

            self.coverpage_button.setDisabled(True)

    def submit(self):
        title = self.book_title_input.text()
        summary = self.book_summary_input.toPlainText()   #get data from input
        points = self.point_requested_input.text()
        self.upload_book.contribute_by = self.user.username
        if not title:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Title is required')
            print("Title is required")
        else:
            self.upload_book.title = title
        if not summary:
            print("Summary is required")
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'summary is required')
        else:
            self.upload_book.summary = summary
        if not points:
            print("Points is required!!")
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'points is required')
        else:
            self.upload_book.requestPoint = points
        if not self.upload_book.cover_page:
            print("cover page required!!")
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'cover page need uploaded!!')
        if not self.upload_book.book_file:
            print("book required!!")
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Book file need uploaded!!')
        if title and summary and points and self.upload_book.book_file and self.upload_book.cover_page:
            self.library.update_book_data(self.upload_book, "pending_book_data.pkl")
            # self.user.own_book.append(self.upload_book)
            # self.library.update_user_data(self.user)
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Congratulations', 'successful!!')
            self.submit_button.setDisabled(True)

    def searchBook(self):
        for i in range(5):
            item = self.top5_List.item(i)
            item.setText(_translate("MainWindow", "", None))
        keyWord = str(self.search_Input.text())
        result = self.library.searchBook(keyWord)
        if len(result) == 0:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Sorry, we can not find any result.')
        else:
            for i in range(len(result)):
                item = self.top5_List.item(i)
                item.setText(_translate("MainWindow", result[i].title, None))


    def retranslateUi(self, superUser):
        superUser.setWindowTitle(_translate("superUser", "Form", None))
        self.search_Button.setText(_translate("superUser", "Search", None))

        self.contributLabel.setText(_translate("superUser", "Contribute Books:", None))
        self.book_title_label.setText(_translate("superUser", "Book Title:", None))
        self.point_requested_label.setText(_translate("superUser", "point Requested:", None))
        self.book_summary_label.setText(_translate("superUser", "Book Summary:", None))
        self.coverpage_button.setText(_translate("superUser", "CoverPage", None))
        self.upload_book_button.setText(_translate("superUser", "Upload Book", None))
        self.submit_button.setText(_translate("superUser", "Submit", None))
        if self.user.superUser == True:
            self.decide_button.setText(_translate("superUser", "decide", None))
            item = self.request_Table.verticalHeaderItem(0)
            item.setText(_translate("superUser", "1", None))
            item = self.request_Table.verticalHeaderItem(1)
            item.setText(_translate("superUser", "2", None))
            item = self.request_Table.verticalHeaderItem(2)
            item.setText(_translate("superUser", "3", None))
            item = self.request_Table.horizontalHeaderItem(0)
            item.setText(_translate("superUser", "User Name", None))
            item = self.request_Table.horizontalHeaderItem(1)
            item.setText(_translate("superUser", "Book title", None))
            item = self.request_Table.horizontalHeaderItem(2)
            item.setText(_translate("superUser", "point requiest", None))
            __sortingEnabled = self.request_Table.isSortingEnabled()
            self.request_Table.setSortingEnabled(False)

            self.set_pending_book_table()

            self.request_Table.setSortingEnabled(__sortingEnabled)
            self.request_List_Label.setText(_translate("superUser", "Book contribute request List:", None))

        if self.user.superUser == False:
            self.approve_button.setText(_translate("superUser", "approve", None))
            self.denied_button.setText(_translate("superUser", "denied", None))
            item = self.request_Table.verticalHeaderItem(0)
            item.setText(_translate("superUser", "1", None))
            item = self.request_Table.verticalHeaderItem(1)
            item.setText(_translate("superUser", "2", None))
            item = self.request_Table.verticalHeaderItem(2)
            item.setText(_translate("superUser", "3", None))
            item = self.request_Table.horizontalHeaderItem(0)
            item.setText(_translate("superUser", "Book title", None))
            item = self.request_Table.horizontalHeaderItem(1)
            item.setText(_translate("superUser", "requested point", None))
            item = self.request_Table.horizontalHeaderItem(2)
            item.setText(_translate("superUser", "SU set point", None))
            __sortingEnabled = self.request_Table.isSortingEnabled()
            self.request_Table.setSortingEnabled(False)

            self.set_pending_book_table_for_register()

            self.request_Table.setSortingEnabled(__sortingEnabled)
            self.request_List_Label.setText(_translate("superUser", "superuser response:", None))


        self.point_Label.setText(_translate("superUser", "Total points:", None))
        self.points_number_Label.setText(_translate("superUser", str(self.user.point), None))
        self.username_Label.setText(_translate("superUser", "Name:", None))
        self.name_In_Label.setText(_translate("superUser", self.user.username, None))
        self.top5_Label.setText(_translate("superUser", "Top 5 Books:", None))
        __sortingEnabled = self.top5_List.isSortingEnabled()
        self.top5_List.setSortingEnabled(False)
        books = self.library.searchTop5()
        for i in range(len(books)):
            item = self.top5_List.item(i)
            item.setText(_translate("MainWindow", books[i].title, None))

        self.top5_List.setSortingEnabled(__sortingEnabled)
        self.history_Label.setText(_translate("superUser", "Reading History:", None))
        __sortingEnabled = self.history_List.isSortingEnabled()
        self.history_List.setSortingEnabled(False)
        item = self.history_List.item(0)
        item.setText(_translate("superUser", "1. Book1", None))
        item = self.history_List.item(1)
        item.setText(_translate("superUser", "2. Book2", None))
        item = self.history_List.item(2)
        item.setText(_translate("superUser", "3. Book3", None))
        item = self.history_List.item(3)
        item.setText(_translate("superUser", "4. Book4", None))
        item = self.history_List.item(4)
        item.setText(_translate("superUser", "5. Book5", None))
        self.history_List.setSortingEnabled(__sortingEnabled)

