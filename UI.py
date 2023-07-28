# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geo.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setFixedSize(408, 323)
        icon = QtGui.QIcon()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowMinimizeButtonHint);
        icon.addPixmap(QtGui.QPixmap("./icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        self.start_pushButton = QtWidgets.QPushButton(dialog)
        self.start_pushButton.setGeometry(QtCore.QRect(90, 160, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.start_pushButton.setFont(font)
        self.start_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.start_pushButton.setObjectName("start_pushButton")
        self.cancel_pushButton = QtWidgets.QPushButton(dialog)
        self.cancel_pushButton.setGeometry(QtCore.QRect(310, 280, 91, 31))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.progress = QtWidgets.QProgressBar(dialog)
        self.progress.setGeometry(QtCore.QRect(50, 250, 321, 23))
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.splitter = QtWidgets.QSplitter(dialog)
        self.splitter.setGeometry(QtCore.QRect(40, 20, 331, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.csv_textBrowser = QtWidgets.QTextBrowser(self.splitter)
        self.csv_textBrowser.setObjectName("csv_textBrowser")
        self.findcsv_pushButton = QtWidgets.QPushButton(self.splitter)
        self.findcsv_pushButton.setObjectName("findcsv_pushButton")
        self.splitter_2 = QtWidgets.QSplitter(dialog)
        self.splitter_2.setGeometry(QtCore.QRect(40, 60, 331, 31))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.tocsv_textBrowser = QtWidgets.QTextBrowser(self.splitter_2)
        self.tocsv_textBrowser.setObjectName("tocsv_textBrowser")
        self.tocsv_pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.tocsv_pushButton.setObjectName("tocsv_pushButton")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(240, 310, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 191, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 130, 231, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "신영근_지오코딩 툴"))
        self.start_pushButton.setText(_translate("dialog", "실행하기"))
        self.cancel_pushButton.setText(_translate("dialog", "취소하기"))
        self.csv_textBrowser.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:500;\">csv 파일 불러오기</span></p></body></html>"))
        self.findcsv_pushButton.setText(_translate("dialog", "찾아보기"))
        self.tocsv_textBrowser.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:500;\">csv 파일 내보내기</span></p></body></html>"))
        self.tocsv_pushButton.setText(_translate("dialog", "내보내기"))
        self.label.setText(_translate("dialog", "Copyright 2020. 신영근 All rights reserved."))
        self.label_2.setText(_translate("dialog", "※주소데이터가 포함된 컬럼을 선택"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
