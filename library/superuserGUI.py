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
import time
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
        self.library.remove_book_with_nobody_read()
        self.upload_book = Book("","",0)
        self.upload_book.contribute_by = self.user
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, superUser):
        """
        This function is create by PyQt4 UI code generator. But we did some change.
        This function set up superuser page GUI.
        :return:
        """
        superUser.setObjectName(_fromUtf8("superUser"))
        if self.user.superUser is True:
            superUser.resize(1350, 615)
        else:
            superUser.resize(800, 615)
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
        self.book_summary_label.setGeometry(QtCore.QRect(360, 250, 93, 16))
        self.book_summary_label.setObjectName(_fromUtf8("book_summary_label"))
        self.book_title_input = QtGui.QLineEdit(superUser)
        self.book_title_input.setGeometry(QtCore.QRect(480, 170, 113, 20))
        self.book_title_input.setObjectName(_fromUtf8("book_title_input"))

        self.book_type_label = QtGui.QLabel(superUser)
        self.book_type_label.setGeometry(QtCore.QRect(630, 180, 71, 21))
        self.book_type_label.setObjectName(_fromUtf8("book_type_label"))
        self.book_type_input = QtGui.QLineEdit(superUser)
        self.book_type_input.setGeometry(QtCore.QRect(630, 210, 113, 20))
        self.book_type_input.setObjectName(_fromUtf8("book_type_input"))

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
        self.upload_book_button.setGeometry(QtCore.QRect(500, 330, 110, 41))
        self.upload_book_button.setObjectName(_fromUtf8("upload_book_button"))
        self.submit_button = QtGui.QPushButton(superUser)
        self.submit_button.setGeometry(QtCore.QRect(630, 330, 111, 41))
        self.submit_button.setObjectName(_fromUtf8("submit_button"))
        self.request_Table = QtGui.QTableWidget(superUser)
        self.request_Table.setGeometry(QtCore.QRect(340, 430, 441, 161))
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

        if self.user.superUser is True:     # check user is superuser or not, for superuser,we add some feature that only superuser need.
            self.request_Table_superuser = QtGui.QTableWidget(superUser)
            self.request_Table_superuser.setGeometry(QtCore.QRect(800, 90, 441, 131))
            self.request_Table_superuser.setObjectName(_fromUtf8("request_Table_superuser"))
            self.request_Table_superuser.setColumnCount(3)
            self.request_Table_superuser.setRowCount(3)
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setVerticalHeaderItem(1, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setVerticalHeaderItem(2, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setHorizontalHeaderItem(1, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setHorizontalHeaderItem(2, item)
            self.request_List_superuser_Label = QtGui.QLabel(superUser)
            self.request_List_superuser_Label.setGeometry(QtCore.QRect(800, 55, 211, 16))
            self.request_List_superuser_Label.setObjectName(_fromUtf8("request_List_superuser_Label"))
            self.decide_button = QtGui.QPushButton(superUser)
            self.decide_button.setGeometry(QtCore.QRect(1150, 100, 71, 31))
            self.decide_button.setObjectName(_fromUtf8("decide_button"))

            self.user_active_table = QtGui.QTableWidget(superUser)
            self.user_active_table.setGeometry(QtCore.QRect(800, 270, 441, 131))
            self.user_active_table.setObjectName(_fromUtf8("user_active_table"))
            self.user_active_table.setColumnCount(3)
            self.user_active_table.setRowCount(3)
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setVerticalHeaderItem(1, item)
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setVerticalHeaderItem(2, item)
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setHorizontalHeaderItem(1, item)
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setHorizontalHeaderItem(2, item)
            self.user_active_Label = QtGui.QLabel(superUser)
            self.user_active_Label.setGeometry(QtCore.QRect(800, 250, 211, 16))
            self.user_active_Label.setObjectName(_fromUtf8("user_active_Label"))
            self.active_button = QtGui.QPushButton(superUser)
            self.active_button.setGeometry(QtCore.QRect(1150, 300, 71, 31))
            self.active_button.setObjectName(_fromUtf8("active_button"))
            self.not_active_button = QtGui.QPushButton(superUser)
            self.not_active_button.setGeometry(QtCore.QRect(1150, 350, 71, 31))
            self.not_active_button.setObjectName(_fromUtf8("not_active_button"))

            self.complain_table = QtGui.QTableWidget(superUser)
            self.complain_table.setGeometry(QtCore.QRect(800, 440, 341, 131))
            self.complain_table.setObjectName(_fromUtf8("complain_table"))
            self.complain_table.setColumnCount(2)
            self.complain_table.setRowCount(3)
            item = QtGui.QTableWidgetItem()
            self.complain_table.setVerticalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.complain_table.setVerticalHeaderItem(1, item)
            item = QtGui.QTableWidgetItem()
            self.complain_table.setVerticalHeaderItem(2, item)
            item = QtGui.QTableWidgetItem()
            self.complain_table.setHorizontalHeaderItem(0, item)
            item = QtGui.QTableWidgetItem()
            self.complain_table.setHorizontalHeaderItem(1, item)
            self.complain_table.horizontalHeader().setStretchLastSection(True)
            self.complain_Label = QtGui.QLabel(superUser)
            self.complain_Label.setGeometry(QtCore.QRect(800, 420, 211, 16))
            self.complain_Label.setObjectName(_fromUtf8("complain_Label"))
            self.accept_complain_button = QtGui.QPushButton(superUser)
            self.accept_complain_button.setGeometry(QtCore.QRect(1150, 460, 71, 30))
            self.accept_complain_button.setObjectName(_fromUtf8("accept_complain_button"))
            self.reject_complain_button = QtGui.QPushButton(superUser)
            self.reject_complain_button.setGeometry(QtCore.QRect(1150, 500, 71, 30))
            self.reject_complain_button.setObjectName(_fromUtf8("reject_complain_button"))
            self.serious_complain_button = QtGui.QPushButton(superUser)
            self.serious_complain_button.setGeometry(QtCore.QRect(1150, 540, 71, 30))
            self.serious_complain_button.setObjectName(_fromUtf8("serious_complain_button"))

            self.user_add_point_label = QtGui.QLabel(superUser)
            self.user_add_point_label.setGeometry(QtCore.QRect(1000, 10, 100, 16))
            self.user_add_point_label.setObjectName(_fromUtf8("user_add_point_label"))
            self.user_add_point_input = QtGui.QLineEdit(superUser)
            self.user_add_point_input.setGeometry(QtCore.QRect(1000, 30, 113, 20))
            self.user_add_point_input.setObjectName(_fromUtf8("user_add_point_input"))
            self.point_for_user_add_point_label = QtGui.QLabel(superUser)
            self.point_for_user_add_point_label.setGeometry(QtCore.QRect(1120, 10, 100, 16))
            self.point_for_user_add_point_label.setObjectName(_fromUtf8("point_for_user_add_point_label"))
            self.point_for_user_add_point_input = QtGui.QLineEdit(superUser)
            self.point_for_user_add_point_input.setGeometry(QtCore.QRect(1120, 30, 113, 20))
            self.point_for_user_add_point_input.setObjectName(_fromUtf8("point_for_user_add_point_input"))
            self.user_add_point_button = QtGui.QPushButton(superUser)
            self.user_add_point_button.setGeometry(QtCore.QRect(1160, 55, 71, 25))
            self.user_add_point_button.setObjectName(_fromUtf8("user_add_point_button"))

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
        self.username_Label.setGeometry(QtCore.QRect(360, 50, 40, 16))
        self.username_Label.setObjectName(_fromUtf8("username_Label"))
        self.name_In_Label = QtGui.QLabel(superUser)
        self.name_In_Label.setGeometry(QtCore.QRect(420, 50, 100, 21))
        self.name_In_Label.setObjectName(_fromUtf8("name_In_Label"))

        self.top5_Label = QtGui.QLabel(superUser)
        self.top5_Label.setGeometry(QtCore.QRect(30, 90, 74, 16))
        self.top5_Label.setObjectName(_fromUtf8("top5_Label"))
        self.top5_List = QtGui.QListWidget(superUser)
        self.top5_List.setGeometry(QtCore.QRect(30, 130, 209, 163))
        self.top5_List.setObjectName(_fromUtf8("top5_List"))
        for i in range(5):
            item = QtGui.QListWidgetItem()
            self.top5_List.addItem(item)
        self.history_Label = QtGui.QLabel(superUser)
        self.history_Label.setGeometry(QtCore.QRect(30, 340, 100, 16))
        self.history_Label.setObjectName(_fromUtf8("history_Label"))
        self.history_List = QtGui.QListWidget(superUser)
        self.history_List.setGeometry(QtCore.QRect(30, 370, 280, 164))
        self.history_List.setObjectName(_fromUtf8("history_List"))




        self.inviter_table = QtGui.QTableWidget(superUser)
        self.inviter_table.setGeometry(QtCore.QRect(550, 30, 230, 100))
        self.inviter_table.setObjectName(_fromUtf8("inviter_table "))
        self.inviter_table.setColumnCount(2)
        self.inviter_table.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.inviter_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.inviter_table.setVerticalHeaderItem(1, item)

        item = QtGui.QTableWidgetItem()
        self.inviter_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.inviter_table.setHorizontalHeaderItem(1, item)

        self.inviter_table_label = QtGui.QLabel(superUser)
        self.inviter_table_label.setGeometry(QtCore.QRect(610, 15, 211, 16))
        self.inviter_table_label.setObjectName(_fromUtf8("user_active_Label"))

        self.accept_Button = QtGui.QPushButton(superUser)
        self.accept_Button.setGeometry(QtCore.QRect(710, 5, 75, 23))
        self.accept_Button.setObjectName(_fromUtf8("accept_Button"))




        for i in range(len(self.user.readingHistory)):
            item = QtGui.QListWidgetItem()
            self.history_List.addItem(item)


        self.retranslateUi(superUser)

        QtCore.QObject.connect(self.search_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchBook)

        QtCore.QObject.connect(self.accept_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accept)

        QtCore.QObject.connect(self.top5_List, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.open_book)
        QtCore.QObject.connect(self.upload_book_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectFile)
        QtCore.QObject.connect(self.coverpage_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectCoverPage)
        QtCore.QObject.connect(self.submit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.submit)
        if self.user.superUser is True:
            QtCore.QObject.connect(self.decide_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.decide)
            QtCore.QObject.connect(self.active_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.active)
            QtCore.QObject.connect(self.not_active_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.not_active)
            QtCore.QObject.connect(self.accept_complain_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accept_complain)
            QtCore.QObject.connect(self.reject_complain_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reject_complain)
            QtCore.QObject.connect(self.serious_complain_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.serious_complain)
            QtCore.QObject.connect(self.user_add_point_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.user_add_point)

        QtCore.QObject.connect(self.approve_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.approve)
        QtCore.QObject.connect(self.denied_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.denied)

        QtCore.QMetaObject.connectSlotsByName(superUser)

    def user_add_point(self):
        """
        This function will add point to user.
        :return:
        """
        username = str(self.user_add_point_input.text())
        point = self.point_for_user_add_point_input.text()
        if not username:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'please input username!')
        elif not point:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'please input point!')
        else:
            number_point = int(point)
            user = self.library.searchUser(username)
            if user:
                user.point += number_point
                self.library.update_user_data(user)
            else:
                QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', "we didn't find user!")

    def accept_complain(self):
        """
        This function will call when superuser click accept in complaint table.
        superuser accept complaint, so number of complaint for book will increase 1,
        then delete that complain and reset complaint table
        :return:
        """
        if self.complain_book:
            self.complain_book.number_of_complaint += 1
            del self.complain_book.complaint[0]
            if self.complain_book.number_of_complaint >= 3:
                self.library.update_book_data(self.complain_book, delete=True)   # delete book from book database
                user_who_contributed = self.library.searchUser(self.complain_book.contribute_by)  # get the user who contributed this book
                user_who_contributed.point -= self.complain_book.requestPoint + 100
                user_who_contributed.number_of_book_delete += 1
                if user_who_contributed.number_of_book_delete >= 2:
                    user_who_contributed.black_list = True
                self.library.update_user_data(user_who_contributed)    # update user data in database
            else:
                self.library.update_book_data(self.complain_book)
            self.set_complaint_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'no complaint!')

    def reject_complain(self):
        """
        This function will reject the complaint.
        :return:
        """
        if self.complain_book:
            del self.complain_book.complaint[0]        # delete that complaint
            self.library.update_book_data(self.complain_book)
            self.set_complaint_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'no complaint!')

    def serious_complain(self):
        """
        This function is for serious complaint, it will delete that book,
        add user who contributed this book to black list.
        :return:
        """
        if self.complain_book:
            self.library.update_book_data(self.complain_book, delete=True)
            user_who_contributed = self.library.searchUser(self.complain_book.contribute_by)  # get the user who contributed this book
            user_who_contributed.black_list = True          # add to black list
            self.library.update_user_data(user_who_contributed)
            self.set_complaint_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'no complaint!')     # if not more complaint

    def accept(self):

        if self.inviter is not None:
            print self.user.inviteDic
            print self.user.inviteDic[self.inviter].values()[0]
            self.user.inviteDic[self.inviter][self.user.inviteDic[self.inviter].keys()[0]] = True

            user_data = self.library.loadUserData()
            for user in user_data:
              if user.username == self.inviter:

                self.user.readingHistory[self.user.inviteDic[self.inviter].keys()[0]]=  0
                print self.user.readingHistory
            self.library.update_user_data(self.user)
            print self.user.inviteDic
            self.inviter = None
            self.set_inviter_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'no invitation!')

    def set_inviter_table(self):
        for index in range(2):
            item = QtGui.QTableWidgetItem()
            self.inviter_table.setItem(index, 0, item)
            item = QtGui.QTableWidgetItem()
            self.inviter_table.setItem(index, 1, item)

            item = self.inviter_table.item(index, 0)
            item.setText(_translate("superUser", "", None))
            item = self.inviter_table.item(index, 1)
            item.setText(_translate("superUser", "", None))
        self.inviter = None
        # self.approve_book = None
        inviter_data = self.user.inviteDic
        if inviter_data:
            index = 0
            for user in inviter_data:
                if inviter_data[user].values()[0] == False:
                #if user.activate is False:
                    if index is 0:
                        self.inviter = user
                    item = QtGui.QTableWidgetItem()
                    self.inviter_table.setItem(index, 0, item)
                    item = QtGui.QTableWidgetItem()
                    self.inviter_table.setItem(index, 1, item)

                    item = self.inviter_table.item(index, 0)
                    item.setText(_translate("User", user, None))
                    item = self.inviter_table.item(index, 1)
                    item.setText(_translate("User",inviter_data[user].keys()[0], None))

                    if index == 1:
                        break
                    else:
                       index += 1

    def active(self):
        """
        This function will activate the new register user.
        :return:
        """
        if self.user_need_activate:
            self.user_need_activate.activate = True
            self.library.update_user_data(self.user_need_activate)  # update user in user database
            self.user_need_activate = None
            self.set_user_active_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'not new user need activate!')

    def not_active(self):
        """
        This function will not activate the user, and delete the user form user database.
        :return:
        """
        if self.user_need_activate:
            self.library.update_user_data(self.user_need_activate, delete=True)   # delete user in database
            self.user_need_activate = None
            self.set_user_active_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'not new user need activate!')

    def approve(self):
        """
        This function will approve the book with superuser response.
        :return:
        """
        if self.approve_book:
            self.library.update_book_data(self.approve_book, "pending_book_data.pkl", delete=True)
            self.library.update_book_data(self.approve_book)
            self.user.point += self.approve_book.superuser_set_point   # user add the point which superuser decide
            self.points_number_Label.setText(_translate("superUser", str(self.user.point), None))   # update user point information in page
            self.user.own_book.append(self.approve_book)

            self.library.update_user_data(self.user)     # update user information in database
            self.set_superuser_response_table()   # refresh table
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'not book need approve!')

    def denied(self):
        """
        This function will denied the book with superuser response.
        :return:
        """
        if self.approve_book:
            self.library.update_book_data(self.approve_book, "pending_book_data.pkl", delete=True)   # delete the book from pending book database
            self.set_superuser_response_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'not book need denied!')

    def decide(self):
        """
        superuser decide the book request point, and add to book.
        :return:
        """
        if self.decide_book:
            item = self.request_Table_superuser.item(0, 2)
            point = int(item.text())             # superuser input point
            self.decide_book.superuser_set_point = point
            self.library.update_book_data(self.decide_book, "pending_book_data.pkl")
            self.set_pending_book_table()
            self.set_superuser_response_table()
        else:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'not book need decide!')

    def set_pending_book_table(self):
        """
        This function set up pending book table.
        :return:
        """
        for index in range(3):
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setItem(index, 0, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setItem(index, 1, item)
            item = QtGui.QTableWidgetItem()
            self.request_Table_superuser.setItem(index, 2, item)
            item = self.request_Table_superuser.item(index, 0)
            item.setText(_translate("superUser", "", None))       # set all box in table to empty first
            item = self.request_Table_superuser.item(index, 1)
            item.setText(_translate("superUser", "", None))
            item = self.request_Table_superuser.item(index, 2)
            item.setText(_translate("superUser", "", None))
        self.decide_book = None
        pending_book = self.library.loadBookData("pending_book_data.pkl")  # get all pending book
        if pending_book:
            index = 0
            for book in pending_book:
                if book.superuser_set_point == 0:   # check if super user didn't set point
                    if index == 0:
                        self.decide_book = book
                    item = QtGui.QTableWidgetItem()
                    self.request_Table_superuser.setItem(index, 0, item)
                    item = QtGui.QTableWidgetItem()
                    self.request_Table_superuser.setItem(index, 1, item)
                    item = QtGui.QTableWidgetItem()
                    self.request_Table_superuser.setItem(index, 2, item)
                    item = self.request_Table_superuser.item(index, 0)
                    item.setText(_translate("superUser", book.contribute_by, None))
                    item = self.request_Table_superuser.item(index, 1)
                    item.setText(_translate("superUser", book.title, None))   # set up book information
                    item = self.request_Table_superuser.item(index, 2)
                    item.setText(_translate("superUser", str(book.requestPoint), None))
                    print(index)
                    if index >= 2:
                        break
                    else:
                        index += 1


    def set_superuser_response_table(self):
        """
        This function set up superuser response table.
        :return:
        """
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
            item.setText(_translate("superUser", "", None))   # set all box in table to empty first
            item = self.request_Table.item(index, 2)
            item.setText(_translate("superUser", "", None))
        self.approve_book = None
        pending_book = self.library.loadBookData("pending_book_data.pkl")
        if pending_book:
            index = 0
            for book in pending_book:
                if book.superuser_set_point != 0 and book.contribute_by == self.user.username:        # check if super user set point
                    if index == 0:
                        self.approve_book = book
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 0, item)
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 1, item)
                    item = QtGui.QTableWidgetItem()
                    self.request_Table.setItem(index, 2, item)
                    item = self.request_Table.item(index, 0)
                    item.setText(_translate("superUser", book.title, None))
                    item = self.request_Table.item(index, 1)
                    item.setText(_translate("superUser", str(book.requestPoint), None))   # set up book information
                    item = self.request_Table.item(index, 2)
                    item.setText(_translate("superUser", str(book.superuser_set_point), None))
                    print(index)
                    if index == 2:
                        break
                    else:
                        index += 1


    def set_user_active_table(self):
        """
        This function set up user activate table.
        :return:
        """
        for index in range(3):
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setItem(index, 0, item)
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setItem(index, 1, item)
            item = QtGui.QTableWidgetItem()
            self.user_active_table.setItem(index, 2, item)
            item = self.user_active_table.item(index, 0)
            item.setText(_translate("superUser", "", None))
            item = self.user_active_table.item(index, 1)
            item.setText(_translate("superUser", "", None))   # set all box in table to empty first
            item = self.user_active_table.item(index, 2)
            item.setText(_translate("superUser", "", None))
        self.user_need_activate = None
        user_data = self.library.loadUserData()   # get all user
        if user_data:
            index = 0
            for user in user_data:
                if user.activate is False:          # check user activate or not
                    if index is 0:
                        self.user_need_activate = user
                    item = QtGui.QTableWidgetItem()
                    self.user_active_table.setItem(index, 0, item)
                    item = QtGui.QTableWidgetItem()
                    self.user_active_table.setItem(index, 1, item)
                    item = QtGui.QTableWidgetItem()
                    self.user_active_table.setItem(index, 2, item)
                    item = self.user_active_table.item(index, 0)
                    item.setText(_translate("superUser", user.username, None))   # set up user information
                    item = self.user_active_table.item(index, 1)
                    item.setText(_translate("superUser", user.password, None))
                    item = self.user_active_table.item(index, 2)
                    item.setText(_translate("superUser", ' ', None))
                    if index == 2:
                        break
                    else:
                        index += 1


    def set_complaint_table(self):
        """
        This function set up complaint table.
        :return:
        """
        for index in range(3):
            item = QtGui.QTableWidgetItem()
            self.complain_table.setItem(index, 0, item)
            item = QtGui.QTableWidgetItem()
            self.complain_table.setItem(index, 1, item)
            item = self.complain_table.item(index, 0)
            item.setText(_translate("superUser", "", None))   # set all box in table to empty first
            item = self.complain_table.item(index, 1)
            item.setText(_translate("superUser", "", None))
        self.complain_book = None
        book_data = self.library.loadBookData()  # get all books
        if book_data:
            index = 0
            for book in book_data:
                if book.complaint:    # check if book got complaint
                    if index is 0:
                        self.complain_book = book
                    item = QtGui.QTableWidgetItem()
                    self.complain_table.setItem(index, 0, item)
                    item = QtGui.QTableWidgetItem()
                    self.complain_table.setItem(index, 1, item)
                    item = self.complain_table.item(index, 0)
                    item.setText(_translate("superUser", book.title, None))  # set up book information
                    item = self.complain_table.item(index, 1)
                    item.setText(_translate("superUser", book.complaint[0], None))
                    if index >= 2:
                        break
                    else:
                        index += 1


    def open_book(self, item):
        book_list = self.library.loadBookData()  #loading all books from book database
        for book in book_list:
            if book.title == str(item.text()):
                self.bookitem = BookPageGUI(book, self.user) #opening the book page for selected book
                self.bookitem.show()
                break
        else:
            print("book not find") #if book title not in catalog then print message book not find


    def selectFile(self): #select a text file to upload book to system
        file_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home') #opening a QTfileDialogue to select file from computer
        if file_name:
            file_name_cut_list = str(file_name).split('/')
            print(file_name_cut_list)
            # if not self.upload_book.book_file:
            print file_name
            shutil.copy(str(file_name), 'PendingBooks') #copying the book file to pending books directory so super
                                #user can decide if book is to be added to catalog or not
            self.upload_book.book_file = file_name_cut_list[-1]
            print(self.upload_book.book_file)
            self.upload_book_button.setDisabled(True)


    def selectCoverPage(self):
        """
        This function select an image file to upload the book cover page
        :return:
        """
        image = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')     # opening a QTFileDialogue to select image form computer
        if image:
            file_name_cut_list = str(image).split('/')
            shutil.copy(str(image), 'CoverPage')      # copying the selected image file to Coverpage database
            self.upload_book.cover_page = file_name_cut_list[-1]
            self.coverpage_button.setDisabled(True)

    def submit(self):
        """
        This function will submit the contribute book form, and check all the input.
        If user fill all input, it will create the book object and save on pending_book_data database.
        :return:
        """
        title = str(self.book_title_input.text())
        summary = str(self.book_summary_input.toPlainText())   #get data from input
        points = int(self.point_requested_input.text())
        book_type = str(self.book_type_input.text())
        self.upload_book.contribute_by = self.user.username
        if not title:              # check if not title
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Title is required')
        else:
            self.upload_book.title = title
        if not summary:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'summary is required')
        else:
            self.upload_book.summary = summary
        if not points:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'points is required')
        else:
            self.upload_book.requestPoint = points
        if not self.upload_book.cover_page:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'cover page need uploaded!!')
        if not self.upload_book.book_file:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Book file need uploaded!!')
        if not book_type:
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Sorry', 'Book type is required!!')
        else:       # if we have type
            self.upload_book.type = book_type    # add type to book object
        if title and summary and points and self.upload_book.book_file and self.upload_book.cover_page:  # check if we have everything
            self.upload_book.last_time_read = time.time()
            self.library.update_book_data(self.upload_book, "pending_book_data.pkl")
            QtGui.QMessageBox.warning(QtGui.QDialog(), 'Congratulations', 'successful!!')
            self.submit_button.setDisabled(True)
            if self.user.superUser is True:
                self.set_pending_book_table()


    def set_top5_list(self):
        """
        This function will check user's reading history first.
        If user has reading history, it will display books which has same type with the last book user read.
        If user has not reading history, it will display books which most people read.
        :return:
        """
        __sortingEnabled = self.top5_List.isSortingEnabled()
        self.top5_List.setSortingEnabled(False)
        reading_history = self.user.readingHistory.keys()
        if reading_history:
            book = self.library.search_book_by_title(reading_history[-1])
            print(book)
            if book:
                books = self.library.search_book_by_type(book.type)
            else:
                books = self.library.searchTop5()
        else:
            books = self.library.searchTop5()
        for i in range(len(books)):
            item = self.top5_List.item(i)
            item.setText(_translate("MainWindow", books[i].title, None))
        self.top5_List.setSortingEnabled(__sortingEnabled)

    def searchBook(self):
        """
        This function is for search book base on keyword user enter in input box.
        It will also set up result to list box.
        :return:
        """
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
        """
        This function is create by PyQt4 UI code generator. But we did some change.
        This function set up superuser page GUI.
        :return:
        """
        superUser.setWindowTitle(_translate("superUser", "Form", None))
        self.search_Button.setText(_translate("superUser", "Search", None))

        self.contributLabel.setText(_translate("superUser", "Contribute Books:", None))
        self.book_title_label.setText(_translate("superUser", "Book Title:", None))
        self.book_type_label.setText(_translate("superUser", "Book Type:", None))
        self.point_requested_label.setText(_translate("superUser", "point Requested:", None))
        self.book_summary_label.setText(_translate("superUser", "Book Summary:", None))
        self.coverpage_button.setText(_translate("superUser", "CoverPage", None))
        self.upload_book_button.setText(_translate("superUser", "Upload Book", None))
        self.submit_button.setText(_translate("superUser", "Submit", None))
        if self.user.superUser is True:      # check user is superuser or not, for superuser,we add some feature that only superuser need.
            self.decide_button.setText(_translate("superUser", "decide", None))
            item = self.request_Table_superuser.verticalHeaderItem(0)
            item.setText(_translate("superUser", "1", None))
            item = self.request_Table_superuser.verticalHeaderItem(1)
            item.setText(_translate("superUser", "2", None))
            item = self.request_Table_superuser.verticalHeaderItem(2)
            item.setText(_translate("superUser", "3", None))
            item = self.request_Table_superuser.horizontalHeaderItem(0)
            item.setText(_translate("superUser", "User Name", None))
            item = self.request_Table_superuser.horizontalHeaderItem(1)
            item.setText(_translate("superUser", "Book title", None))
            item = self.request_Table_superuser.horizontalHeaderItem(2)
            item.setText(_translate("superUser", "point requiest", None))
            __sortingEnabled = self.request_Table_superuser.isSortingEnabled()
            self.request_Table_superuser.setSortingEnabled(False)

            self.set_pending_book_table()
            self.request_Table_superuser.setSortingEnabled(__sortingEnabled)
            self.request_List_superuser_Label.setText(_translate("superUser", "Book contribute request List:", None))

            self.active_button.setText(_translate("superUser", "activate", None))
            self.not_active_button.setText(_translate("superUser", "delete", None))
            item = self.user_active_table.verticalHeaderItem(0)
            item.setText(_translate("superUser", "1", None))
            item = self.user_active_table.verticalHeaderItem(1)
            item.setText(_translate("superUser", "2", None))
            item = self.user_active_table.verticalHeaderItem(2)
            item.setText(_translate("superUser", "3", None))
            item = self.user_active_table.horizontalHeaderItem(0)
            item.setText(_translate("superUser", "User Name", None))
            item = self.user_active_table.horizontalHeaderItem(1)
            item.setText(_translate("superUser", "password", None))
            item = self.user_active_table.horizontalHeaderItem(2)
            item.setText(_translate("superUser", " ", None))
            __sortingEnabled = self.user_active_table.isSortingEnabled()
            self.user_active_table.setSortingEnabled(False)

            self.set_user_active_table()     # set up user activate table
            self.user_active_table.setSortingEnabled(__sortingEnabled)
            self.user_active_Label.setText(_translate("superUser", "new register user List:", None))

            self.accept_complain_button.setText(_translate("superUser", "accept", None))
            self.reject_complain_button.setText(_translate("superUser", "reject", None))
            self.serious_complain_button.setText(_translate("superUser", "punish", None))
            item = self.complain_table.verticalHeaderItem(0)
            item.setText(_translate("superUser", "1", None))
            item = self.complain_table.verticalHeaderItem(1)
            item.setText(_translate("superUser", "2", None))
            item = self.complain_table.verticalHeaderItem(2)
            item.setText(_translate("superUser", "3", None))
            item = self.complain_table.horizontalHeaderItem(0)
            item.setText(_translate("superUser", "book title", None))
            item = self.complain_table.horizontalHeaderItem(1)
            item.setText(_translate("superUser", "complaint reason", None))

            self.set_complaint_table()       # set up complaint_table
            __sortingEnabled = self.complain_table.isSortingEnabled()
            self.complain_table.setSortingEnabled(False)

            self.complain_table.setSortingEnabled(__sortingEnabled)
            self.complain_Label.setText(_translate("superUser", "complaint List:", None))

            self.user_add_point_label.setText(_translate("superUser", "username", None))
            self.point_for_user_add_point_label.setText(_translate("superUser", "point", None))
            self.user_add_point_button.setText(_translate("superUser", "Add", None))

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

        self.set_superuser_response_table()

        self.request_Table.setSortingEnabled(__sortingEnabled)
        self.request_List_Label.setText(_translate("superUser", "superuser response:", None))

        self.point_Label.setText(_translate("superUser", "Total points:", None))
        self.points_number_Label.setText(_translate("superUser", str(self.user.point), None))
        self.username_Label.setText(_translate("superUser", "Name:", None))
        self.name_In_Label.setText(_translate("superUser", self.user.username, None))

       # self.inviter_name.setText(_translate("superUser", self.user.inviteDic.username, None))


        self.accept_Button.setText(_translate("superUser", "accept", None))

        self.top5_Label.setText(_translate("superUser", "recommended books or top 5 Books:", None))

        self.set_top5_list()   # set up top 5 list


        self.history_Label.setText(_translate("superUser", "Reading History:", None))
        __sortingEnabled = self.history_List.isSortingEnabled()
        self.history_List.setSortingEnabled(False)

        i=0
        for key, value in self.user.readingHistory.items():
        #for i in range(len(self.user.readingHistory)):
            item = self.history_List.item(i)
            item.setText(_translate("superUser", key + "    Status:You have "+ str(value) + " mins remained!" , None))
            i += 1

        self.history_List.setSortingEnabled(__sortingEnabled)

        self.accept_Button.setText(_translate("User", "accept", None))
        item = self.inviter_table.verticalHeaderItem(0)
        item.setText(_translate("User", "1", None))
        item = self.inviter_table.verticalHeaderItem(1)
        item.setText(_translate("User", "2", None))

        item = self.inviter_table.horizontalHeaderItem(0)
        item.setText(_translate("User", "InviterName", None))
        item = self.inviter_table.horizontalHeaderItem(1)
        item.setText(_translate("User", "BookName", None))

        __sortingEnabled = self.inviter_table.isSortingEnabled()
        self.inviter_table.setSortingEnabled(False)

        self.set_inviter_table()
        self.inviter_table.setSortingEnabled(__sortingEnabled)
        self.inviter_table_label.setText(_translate("User", "Inviter List:", None))
