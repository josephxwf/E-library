# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookpage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class BookPageGUI(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 647)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 30, 271, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 280, 111, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(70, 70, 151, 191))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 520, 481, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 600, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(270, 100, 261, 101))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.textBrowser = QtGui.QTextBrowser(self.widget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(270, 80, 92, 14))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.widget2 = QtGui.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(270, 210, 188, 14))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.widget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.widget2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.widget3 = QtGui.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(50, 320, 481, 191))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_8 = QtGui.QLabel(self.widget3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.textBrowser_2 = QtGui.QTextBrowser(self.widget3)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayout_2.addWidget(self.textBrowser_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "intro to python", None))
        self.label_3.setText(_translate("Form", "rate this book", None))
        self.pushButton.setText(_translate("Form", "read", None))
        self.label_9.setText(_translate("Form", "covepage", None))
        self.pushButton_2.setText(_translate("Form", "submit", None))
        self.label_4.setText(_translate("Form", "Summary:", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">afafafag</p></body></html>", None))
        self.label_2.setText(_translate("Form", "Author:", None))
        self.label_6.setText(_translate("Form", "kaiying", None))
        self.label_5.setText(_translate("Form", "Point for reading this book:", None))
        self.label_7.setText(_translate("Form", "50", None))
        self.label_8.setText(_translate("Form", "comments", None))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     bookPage = QtGui.QWidget()
#     ui = BookpageGUI()
#     ui.setupUi(bookPage)
#     bookPage.show()
#     sys.exit(app.exec_())
#
