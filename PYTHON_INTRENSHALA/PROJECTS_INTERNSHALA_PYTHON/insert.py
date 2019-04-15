# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from success import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(257, 155)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.book = QtWidgets.QLineEdit(Form)
        self.book.setObjectName("book")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.book)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.author = QtWidgets.QLineEdit(Form)
        self.author.setObjectName("author")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.author)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setObjectName("price")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.price)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.stock = QtWidgets.QLineEdit(Form)
        self.stock.setObjectName("stock")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.stock)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.insert = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.insert.setFont(font)
        self.insert.setObjectName("insert")
        self.insert.clicked.connect(self.getData)
        self.horizontalLayout_3.addWidget(self.insert)
        self.clear = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.horizontalLayout_3.addWidget(self.clear)
        self.cancel = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        #self.cancel.clicked.connect(sys.exit(app.exec_()))
        self.horizontalLayout_3.addWidget(self.cancel)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_3)

        self.retranslateUi(Form)
        self.clear.clicked.connect(self.book.clear)
        self.clear.clicked.connect(self.author.clear)
        self.clear.clicked.connect(self.price.clear)
        self.clear.clicked.connect(self.stock.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Book"))
        self.label_2.setText(_translate("Form", "Author"))
        self.label_3.setText(_translate("Form", "Price"))
        self.label_4.setText(_translate("Form", "Stock"))
        self.insert.setText(_translate("Form", "Insert"))
        self.clear.setText(_translate("Form", "Clear"))
        self.cancel.setText(_translate("Form", "Cancel"))

    def getData(self):
        try:
            conc = sqlite3.connect('books.db')
            t = self.book.text()
            a = self.author.text()
            p = self.price.text()
            s = self.stock.text()
            sql = ("INSERT INTO Books (Title, Author, Price, Available) VALUES ('{}', '{}', {}, {});".format(t, a, p, s))
            curbook = conc.cursor()
            curbook.execute(sql)
            conc.close()
            print("success")
        except:
            print("Error")

    def dail(self):
        self.QDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(Dialog)
        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())




        
       
      
      
       
          
        
        


