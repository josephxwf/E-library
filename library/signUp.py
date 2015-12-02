# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created: Sat Nov 28 01:30:17 2015
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!
from User import User
import pickle
from PyQt4 import QtCore, QtGui
from User import User

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s




class SignUp(QtGui.QDialog):
    def __init__(self, library):
        self.library = library
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 131, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 113, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(122, 100, 111, 21))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 150, 113, 21))
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 81, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 200, 81, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 60, 131, 20))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 100, 131, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(170, 180, 250, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.signup)


        QtCore.QMetaObject.connectSlotsByName(Form)


    def signup(self):
        username = self.lineEdit.text()  #get data from input
        password1 = self.lineEdit_2.text()
        password2 =  self.lineEdit_3.text()
        if not username:
            self.label_4.setText(_fromUtf8("Username is required!"))
            print("username is required")
        elif not password1:
            self.label_5.setText(_fromUtf8("Password is required!"))
            print("password is required")
        elif password1 != password2:
            self.label_6.setText(_fromUtf8("Password1 and Password2 are dfferent!"))
            print("Password1 and Password2 are dfferent!")
        else:
            with open('company_data.pkl', 'a') as output:
                user = User(username, password1)
                pickle.dump(user, output)



                del user
                self.hide()
          #with open("userDatabase.txt",'a') as file_handle:
        #     file_handle.write(str(0) + " " + str(0) + " " + username + " " + password1 + "\n")
        #


    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Confirm Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Signup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
#
# <<<<<<< HEAD
#
#     def setupUi(self, Dialog):
#         Dialog.setObjectName(_fromUtf8("Sign Up"))
#         Dialog.resize(400, 300)
#         self.signButton = QtGui.QPushButton(Dialog)
#         self.signButton.setGeometry(QtCore.QRect(111, 161, 75, 23))
#         self.signButton.setObjectName(_fromUtf8("signButton"))
#         self.cancelButton = QtGui.QPushButton(Dialog)
#         self.cancelButton.setGeometry(QtCore.QRect(192, 161, 75, 23))
#         self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
#         self.widget = QtGui.QWidget(Dialog)
#         self.widget.setGeometry(QtCore.QRect(60, 50, 245, 80))
#         self.widget.setObjectName(_fromUtf8("widget"))
#         self.verticalLayout = QtGui.QVBoxLayout(self.widget)
#         self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
#         self.horizontalLayout = QtGui.QHBoxLayout()
#         self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
#         self.usernameLabel = QtGui.QLabel(self.widget)
#         self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
#         self.horizontalLayout.addWidget(self.usernameLabel)
#         self.usernameInput = QtGui.QLineEdit(self.widget)
#         self.usernameInput.setObjectName(_fromUtf8("usernameInput"))
#         self.horizontalLayout.addWidget(self.usernameInput)
#         self.verticalLayout.addLayout(self.horizontalLayout)
#         self.horizontalLayout_2 = QtGui.QHBoxLayout()
#         self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
#         self.pwLabel = QtGui.QLabel(self.widget)
#         self.pwLabel.setObjectName(_fromUtf8("pwLabel"))
#         self.horizontalLayout_2.addWidget(self.pwLabel)
#         self.pwInput = QtGui.QLineEdit(self.widget)
#         self.pwInput.setEchoMode(QtGui.QLineEdit.Password)
#         self.pwInput.setObjectName(_fromUtf8("pwInput"))
#         self.horizontalLayout_2.addWidget(self.pwInput)
#         self.verticalLayout.addLayout(self.horizontalLayout_2)
#         self.horizontalLayout_3 = QtGui.QHBoxLayout()
#         self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
#         self.confirmPwLabel = QtGui.QLabel(self.widget)
#         self.confirmPwLabel.setObjectName(_fromUtf8("confirmPwLabel"))
#         self.horizontalLayout_3.addWidget(self.confirmPwLabel)
#         self.confirmPwInput = QtGui.QLineEdit(self.widget)
#         self.confirmPwInput.setText(_fromUtf8(""))
#         self.confirmPwInput.setEchoMode(QtGui.QLineEdit.Password)
#         self.confirmPwInput.setObjectName(_fromUtf8("confirmPwInput"))
#         self.horizontalLayout_3.addWidget(self.confirmPwInput)
#         self.verticalLayout.addLayout(self.horizontalLayout_3)
#
#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#         QtCore.QObject.connect(self.signButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.signUp)
#
#     def signUp(self):
#         username = self.usernameInput.text()
#         password = self.pwInput.text()
#         confirmPw = self.confirmPwInput.text()
#         if not username:
#             print("username is required")
#         elif not password:
#             print("password is required")
#         elif not confirmPw:
#             print("confirmPW required")
#         elif password != confirmPw:
#             print("two password not same")
#         else:
#             flag = False
#             for user in self.library.userData:
#                 if username == user.username:
#                     print("username is already used")
#                     flag = True
#                     break
#             if flag == False:
#                 self.library.userData.append(User(username, password))
#                 print("success")
#                 self.close()
#
#
#
#
#     def retranslateUi(self, Dialog):
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
#         self.signButton.setText(_translate("Dialog", "sign Up", None))
#         self.cancelButton.setText(_translate("Dialog", "cancel", None))
#         self.usernameLabel.setText(_translate("Dialog", "username:", None))
#         self.pwLabel.setText(_translate("Dialog", "password:", None))
#         self.confirmPwLabel.setText(_translate("Dialog", "confirm password:", None))
# =======
# >>>>>>> 000b0d78377b02e9ef52c9b85616c9278a57275f
#
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = SignUp()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
