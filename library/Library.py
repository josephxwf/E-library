from User import User
from Book import Book
import pickle
#import os
# from PyQt4 import QtCore, QtGui
# from visitorGUI import Visitor_MainWindow
# from bookpageGUI import BookpageGUI
# import sys
#
#
# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s
#
# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)
#

class Library():
    def __init__(self):    #constructor
        self.userData = self.loadUserData()
        self.bookData = self.loadBookData()

    def update_user_data(self, new_user):
        """
        This function will updata user object in user database
        :param new_user: user object which need update
        :return:
        """
        userData = self.loadUserData()
        newData = []
        find = False
        for user in userData:
            if user.username == new_user.username:
                newData.append(new_user)
                find = True
            else:
                newData.append(user)
        if find is False:
            newData.append(new_user)

        with open('user_data.pkl', 'w') as output:
            pickle.dump(newData, output)

    def loadUserData(self):
        """
        This function will load all user object from user database.

        :return: user object list
        """
        try:
            with open('user_data.pkl', 'r') as input:
                try:
                    user = pickle.load(input)
                except:
                    user = None
        except:
            user=None
            with open('user_data.pkl', 'w') as output:
                pass
        return user

    def loadBookData(self, path='book_data.pkl'):
        """
        This function will load all book object from book database.

        :param path: string type, path of database
        :return: book object list
        """
        try:
            with open(path, 'r') as input:
                try:
                    book = pickle.load(input)
                except:
                    book = None
        except:
            book = None
            with open(path, 'w') as output:
                pass

        return book

    def update_book_data(self, new_book, path='book_data.pkl', delete=False):
        """
        this function will updata book database
        :param new_book: book object which need update
        :param path: string type, path of book database
        :param delete: boolean, if true, it will delete book object
        :return:
        """
        book_data = self.loadBookData(path)
        new_data = []
        find = False
        if book_data:
            for book in book_data:
                if book.title == new_book.title:
                    if delete == False:
                        new_data.append(new_book)
                    find = True
                else:
                    new_data.append(book)
            if find is False:
                new_data.append(new_book)
        else:
            new_data.append(new_book)

        with open(path, 'w') as output:
            pickle.dump(new_data, output)


    def searchBook(self, keyword):
        '''
        :param title:
        :return: book
        '''
        result = []
        resultNum = 5

        bookData = self.loadBookData()
        if bookData:
            for book in bookData:
                if keyword.lower() in book.title.lower(): #maybe need to convert keyword to str(keyword)
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in str(book.author).lower():
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in str(book.type).lower():
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in str(book.summary).lower():
                    result.append(book)
                    resultNum -=1
                if resultNum == 0:
                    break
        return result

    def searchUser(self, name):
        """
        This function will return user object by input string type username

        :param string (username)
        :return: user object
        """
        users = self.loadUserData() # load all users from database
        for user in users:
            if user.username == name:
                return user
        return None

    def searchTop5(self):
        top5List = []
        book_data = self.loadBookData()
        if book_data:
            data = sorted(book_data, key=lambda book: book.NumOfRead, reverse=True)
            for i in range(len(data)):
                top5List.append(data[i])
                #print i
        return top5List

    def Catalog(self):
        BookList = []
        book_data = self.loadBookData()
        if book_data:
            bookdata = sorted(book_data, key=lambda book: book.title, reverse=True)
            for i in range(len(bookdata)):  #need to make the range equal total number of books in self.bookData
                BookList.append(bookdata[i])
        return BookList
# if __name__ == '__main__':
#     mylibrary = Library()
#     top5 = mylibrary.searchTop5()
#     for i in range(5):
#         print(top5[i].title)


#     Library()
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     visitorGUI = Visitor_MainWindow()
#     visitorGUI.setupUi(MainWindow)
#
#
#
#     MainWindow.show()
#     sys.exit(app.exec_())
