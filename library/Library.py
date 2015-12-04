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

# <<<<<<< HEAD
#     def saveUserData(self):
#         pass
# =======
#     #def makebooksdatabase(self):
#     #    os.mkdir('Database')
#     #    os.mkdir('PendingBooks')
# >>>>>>> 8a0412333e7be461d43c0f98a57fad3889c12a70
#
    def loadUserData(self):
        user_list = []
        with open('user_data.pkl', 'r') as input:
            user = pickle.load(input)
            while(user):
                user_list.append(user)
                try:
                    user = pickle.load(input)
                except:
                    user = None
        return user_list

    def loadBookData(self):
        book_list = []
        with open('book_data.pkl', 'r') as input:
            book = pickle.load(input)
            while(book):
                book_list.append(book)
                try:
                    book = pickle.load(input)
                except:
                    book = None
        return book_list


    def searchBook(self, keyword):
        '''
        :param title:
        :return: book
        '''
        result = []
        resultNum = 5
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
