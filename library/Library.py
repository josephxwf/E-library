from User import User
from Book import Book
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
    def __init__(self):
        self.userData = self.loadUserData()
        print(self.userData[0].username)
        self.bookData = self.loadBookData()
        print(self.bookData[0].title)
        self.top5Book = self.searchTop5()



    def loadUserData(self):
        fakeUserData = [User("a","a"),User("b","b") ]
        return fakeUserData

    def loadBookData(self):
        fakeBookData = []
        books = Book("a title 1",50)
        books.NumOfRead = 10
        fakeBookData.append(books)
        books = Book("a title 2",110)
        books.NumOfRead = 13
        fakeBookData.append(books)
        books = Book("a title 3",10)
        books.NumOfRead = 5
        fakeBookData.append(books)
        books = Book("a title 4",10)
        books.NumOfRead = 44
        fakeBookData.append(books)
        books = Book("a title 5",10)
        books.NumOfRead = 1
        fakeBookData.append(books)
        # print(fakeBookData)
        return fakeBookData


    def searchBook(self, keyword):
        '''
        :param title:
        :return: book
        '''
        result = []
        resultNum = 5
        for book in self.bookData:
            if keyword in book.title:
                result.append(book)
                resultNum -=1
            elif keyword in book.author:
                result.append(book)
                resultNum -=1
            elif keyword in book.description:
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
        return top5List


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