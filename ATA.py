# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATA.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import requests
import json
import re

from bs4 import BeautifulSoup

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
        
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(1065, 752)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(320, 670, 701, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.search_text)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 680, 211, 21))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 971, 581))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 620, 101, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 620, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 620, 81, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 620, 211, 29))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(670, 620, 281, 29))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Alexa Teaching Assistant"))
        self.label.setText(_translate("Dialog", "Type your query here:"))
        instr_data = self.read_instr_input()

        
        
        self.instr_data_text = instr_data['results']['transcripts'][0]['transcript']

        self.instr_data_text0 = self.instr_data_text[:]
        
        start_time = instr_data['results']['items'][0]['start_time']
        end_time = instr_data['results']['items'][0]['end_time']

        self.time_text = '<font color="red">Start Time: ' + start_time + ', End Time: ' + end_time + '</font>&ensp;'

        '''self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.time_text + self.instr_data_text + "</p></body></html>"))'''


        self.set_text()

        self.label_2.setText(_translate("Dialog", "Highlight"))
        self.comboBox.setItemText(0, _translate("Dialog", "Today"))
        self.comboBox.setItemText(1, _translate("Dialog", "Last 5 min"))
        self.comboBox.setItemText(2, _translate("Dialog", "Last 15 min"))
        self.comboBox.setItemText(3, _translate("Dialog", "Last week"))
        self.comboBox.setItemText(4, _translate("Dialog", "Entire semester"))
        self.label_3.setText(_translate("Dialog", "Email"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Today\'s lecture to me"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Last week lectures to me"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Entire lectures to me"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Query to Instructor"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Query and last 15 minutes to Instructor"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Query and Today\'s lecture to Instructor"))


    def set_text(self):
 
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.time_text + self.instr_data_text + "</p></body></html>"))

    def read_instr_input(self):

        input_data = json.load(open('instr_input.json'))
        return (input_data)


    def search_text(self):
        # print('OH BOY: I search: ' + self.instr_data_text)
        
        ttt = self.lineEdit.text()
        

        if len(ttt) == 0:
            self.instr_data_text = self.instr_data_text0[:]
            self.set_text()
            return
        

        self.instr_data_text = self.instr_data_text0[:]
        self.instr_data_text = re.sub(ttt, r'<font color=blue><b>' + ttt + '</b></font>', self.instr_data_text, flags = re.IGNORECASE)
        
        self.set_text()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

