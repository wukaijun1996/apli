# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radius.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()

        self.setupUi(self)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(716, 441)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 241, 21))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 51, 31))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.label.setStyleSheet("font-size: 20;color:red;")
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(160, 170, 381, 181))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "吴开开"))
        self.label.setText(_translate("Dialog", "圆的半径"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        # 绑定事件
        self.pushButton.clicked.connect(self.click_handle)

    def click_handle(self):
        # 获取输入的半径
        radius = self.lineEdit.text().strip()

        try:
            ret = float(radius) ** 2 * 3.14

        except Exception as f:
            print("请输入整数或小数")

        #显示
        self.textEdit.append('{}半径的面积为{}'.format(radius,ret))




if __name__ == '__main__':
    # 主进程
    app = QtWidgets.QApplication(sys.argv)
    # 主进程的对话框   app 是QtWidget控件显示的上下文的环境
    dialog = Ui_Dialog()
    dialog.show()   #显示对话框

    sys.exit(app.exec_())