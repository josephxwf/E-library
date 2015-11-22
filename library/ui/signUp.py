# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUp.ui'
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

class SignUp(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.signButton = QtGui.QPushButton(Dialog)
        self.signButton.setGeometry(QtCore.QRect(111, 161, 75, 23))
        self.signButton.setObjectName(_fromUtf8("signButton"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(192, 161, 75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 50, 245, 80))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.usernameLabel = QtGui.QLabel(self.widget)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.horizontalLayout.addWidget(self.usernameLabel)
        self.usernameInput = QtGui.QLineEdit(self.widget)
        self.usernameInput.setObjectName(_fromUtf8("usernameInput"))
        self.horizontalLayout.addWidget(self.usernameInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pwLabel = QtGui.QLabel(self.widget)
        self.pwLabel.setObjectName(_fromUtf8("pwLabel"))
        self.horizontalLayout_2.addWidget(self.pwLabel)
        self.pwInput = QtGui.QLineEdit(self.widget)
        self.pwInput.setEchoMode(QtGui.QLineEdit.Password)
        self.pwInput.setObjectName(_fromUtf8("pwInput"))
        self.horizontalLayout_2.addWidget(self.pwInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.confirmPwLabel = QtGui.QLabel(self.widget)
        self.confirmPwLabel.setObjectName(_fromUtf8("confirmPwLabel"))
        self.horizontalLayout_3.addWidget(self.confirmPwLabel)
        self.confirmPwInput = QtGui.QLineEdit(self.widget)
        self.confirmPwInput.setText(_fromUtf8(""))
        self.confirmPwInput.setEchoMode(QtGui.QLineEdit.Password)
        self.confirmPwInput.setObjectName(_fromUtf8("confirmPwInput"))
        self.horizontalLayout_3.addWidget(self.confirmPwInput)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.signButton.setText(_translate("Dialog", "sign Up", None))
        self.cancelButton.setText(_translate("Dialog", "cancel", None))
        self.usernameLabel.setText(_translate("Dialog", "username:", None))
        self.pwLabel.setText(_translate("Dialog", "password:", None))
        self.confirmPwLabel.setText(_translate("Dialog", "confirm password:", None))

#
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Dialog = QtGui.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
#
