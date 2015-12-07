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
        self.top5Book = self.searchTop5()
        self.allbooks = self.Catalog()

    def update_user_data(self, new_user):
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
        with open('user_data.pkl', 'r') as input:
            try:
                user = pickle.load(input)
            except:
                user = None
        return user

    def loadBookData(self, path='book_data.pkl'):
        with open(path, 'r') as input:
            try:
                book = pickle.load(input)
            except:
                book = None

        return book

    def update_book_data(self, new_book, path='book_data.pkl'):
        book_data = self.loadBookData()
        new_data = []
        find = False
        for book in book_data:
            if book.title == new_book.title:
                new_data.append(new_data)
                find = True
            else:
                new_data.append(book)
        if find is False:
            new_data.append(new_book)

        with open(path,'w') as output:
            pickle.dump(new_data, output)


    def searchBook(self, keyword):
        '''
        :param title:
        :return: book
        '''
        result = []
        resultNum = 5
        if self.bookData:
            for book in self.bookData:
                if keyword.lower() in book.title.lower():
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in book.author.lower():
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in book.type.lower():
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in book.summary.lower():
                    result.append(book)
                    resultNum -=1
                if resultNum == 0:
                    break
        return result

    def searchUser(self, name):
        '''
        :param name:
        :return: user
        '''

    def searchTop5(self):
        top5List = []
        data = sorted(self.bookData, key=lambda book: book.NumOfRead, reverse=True)
        # print(data)
        for i in range(5):
            top5List.append(data[i])
            #print i
        return top5List

    def Catalog(self):
        BookList = []
        bookdata = sorted(self.bookData, key=lambda book: book.title, reverse=True)
        for i in range(5):  #need to make the range equal total number of books in self.bookData
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
