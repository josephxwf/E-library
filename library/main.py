from Library import Library
from PyQt4 import QtCore, QtGui
import visitorGUI
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
    # MainWindow.close()
    sys.exit(app.exec_())