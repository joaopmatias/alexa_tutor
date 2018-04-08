# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alexa_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


import requests
import json
import re

import time

from bs4 import BeautifulSoup

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import smtplib



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1026, 842)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 1001, 731))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 760, 96, 27))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 760, 151, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(390, 760, 621, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.search_text)

        self.lineEdit.textChanged.connect(self.search_text)
        self.pushButton.clicked.connect(self.update_info)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 800, 241, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.send_transcript_to_self)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 800, 361, 27))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.send_transcript_to_self)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.update_info()



        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.ehlo()
            self.server.login('alexatutor8@gmail.com', 'alokjoaopm')

        except:
            print('No E-mail Connection')

    def update_info(self):
    
        with open("all.txt") as f:
            lines = f.readlines()

            lines = [line.strip() for line in lines]
            lines = [line for line in lines if len(line) != 0]

            self.set_text(lines)

        self.lineEdit.clear()

    def send_transcript_to_self(self):
        try:

            subject = 'Alexa Tutor Transcript'
            message = 'Subject: {}\n\n{}'.format(subject, self.raw_text)

            

            self.server.sendmail('alexatutor8@gmail.com', 'alexatutor8@gmail.com', message)
        except:
            pass



    def set_text(self, lines):


        self.text_str = ''
        self.raw_text = ''

        for line in lines:
            self.text_str = self.text_str + line + '<br />'
            self.raw_text = self.raw_text + line + '\n'
            self.text_str0 = self.text_str[:]

            
        _translate = QtCore.QCoreApplication.translate

        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.text_str + "</p></body></html>"))



    def update_search_text(self):

                
        _translate = QtCore.QCoreApplication.translate

        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.text_str + "</p></body></html>"))


    def search_text(self):
                

        ttt = self.lineEdit.text()


        if len(ttt) == 0:
            self.text_str = self.text_str0[:]
            self.update_search_text()
            return


        
        self.text_str = self.text_str0[:]
        
        self.text_str = re.sub(ttt, r'<font color=blue><b>' + ttt + '</b></font>', self.text_str, flags = re.IGNORECASE)
        
        self.update_search_text()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Alexa Tutor"))
        self.pushButton.setText(_translate("Dialog", "Update"))
        self.label.setText(_translate("Dialog", "Search Transcript"))
        self.pushButton_2.setText(_translate("Dialog", "Email Transcript to Self"))
        self.pushButton_3.setText(_translate("Dialog", "Email Query to Instructor"))

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)


    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    Dialog.setWindowIcon(QtGui.QIcon('Tutor.jpg'))
    Dialog.show()

    sys.exit(app.exec_())




