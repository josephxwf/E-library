from Library import Library
# from User import User
# from Book import Book
from PyQt4 import QtCore, QtGui
import visitorGUI
# from bookpageGUI import BookpageGUI
import sys


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



if __name__ == '__main__':
    library = Library()
    mainUser = None
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    visitorGUI = visitorGUI.Visitor_MainWindow(library)
    # visitorGUI.library = library
    visitorGUI.setupUi(MainWindow)
    MainWindow.show()
    print("aaaa")
    print(visitorGUI.user)
    # MainWindow.close()
    sys.exit(app.exec_())



#
#
# if __name__ == '__main__':
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
