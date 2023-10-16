# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\muzamil image\Desktop\ez.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from time import localtime, strftime
import sys
from PyQt5 import QtWidgets, QtGui
from time import ctime
import datetime
from keras.models import load_model
import numpy as np
import scipy.misc
modell = load_model('AI Training Module.h5')
filename = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1431, 946)
        MainWindow.setStyleSheet("background-color: rgb(205, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 361, 141))
        self.logo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.logo.setFrameShape(QtWidgets.QFrame.Box)
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(370, 10, 1291, 141))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.textEdit.setFont(font)

        self.textEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
    "font: italic 8pt \"MS Sans Serif\";")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)

        self.selectImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn.setGeometry(QtCore.QRect(110, 260, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.selectImageBtn.setFont(font)
        self.selectImageBtn.setStyleSheet("background-color: rgb(170, 170, 255);\n"
    "font: 20pt \"Times New Roman\";\n"
    "")
        self.selectImageBtn.setObjectName("selectImageBtn")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(520, 200, 621, 321))
        self.imageLbl.setStyleSheet("background-color: rgb(185, 186, 208);")
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(120, 730, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("background-color: rgb(170, 170, 255);\n"
    "font: 20pt \"Times New Roman\";")
        self.addBtn.setObjectName("addBtn")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(520, 640, 621, 251))
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setStyleSheet("background-color: rgb(170, 170, 255);\n""font: italic 28pt \"MS Sans Serif\";"
    "color: rgb(0, 0, 0);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setLineWidth(4)
        self.listWidget.setObjectName("listWidget")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(1460, 10, 745, 141))
        self.time.setStyleSheet("color: rgb(255, 255, 255);\n""font: italic 28pt \"MS Sans Serif\";"
    "background-color: rgb(0, 0, 0);")
        self.time.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time.setText("")
        self.time.setObjectName("time")
        #self.time.setText("%s" % strftime("%a, %d %b %Y %H:%M:%S ", localtime()))
        #self.time.setText("%s" % ctime())
        self.time.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "color: rgb(255, 255, 255);\n"
                                "background-color: rgb(0, 0, 0);""font: italic 28pt \"MS Sans Serif\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1431, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.logo.setPixmap(QtGui.QPixmap('New.png'))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1564, 151, 341, 825))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(QtGui.QPixmap('a.png'))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectImageBtn.clicked.connect(self.setImage)
        self.addBtn.clicked.connect(self.addItem)




    def retranslateUi(self, MainWindow):
        now = datetime.datetime.now()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "controlEz Articial Inteligence"))
        self.time.setText(_translate("MainWindow", now.strftime("%Y-%m-%d %H:%M:%S"), None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:8pt; font-weight:400; font-style:italic;\">\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-style:normal;\"><br /></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; color:#ffffff;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; color:#ffffff;\">       Control Easy Artificial Intelligence (AI)</span></p></body></html>"))
        self.selectImageBtn.setText(_translate("MainWindow", "Select Image"))
        self.addBtn.setText(_translate("MainWindow", "Test"))

    def setImage(self):
        global filename
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
        if filename:  # If the user gives a file
            pixmap = QtGui.QPixmap(filename)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.imageLbl.setPixmap(pixmap)  # Set the pixmap onto the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
            self.listWidget.clear()


    def addItem(self):
        global filename
        if filename:
            imgs = [scipy.misc.imresize(scipy.misc.imread(filename), (150, 150))]
            data = np.array(imgs) / 255
            history2 = modell.predict_proba(data, batch_size=20, verbose=True)
            for pred in history2:
                if history2[0, 0] > 0.66:
                    self.listWidget.addItem("Potato")
                    self.listWidget.addItem(str(round(history2[0, 0]*100, 4)))
                elif history2[0, 1] > 0.66:
                    self.listWidget.addItem('Apple')
                    self.listWidget.addItem(str(round(history2[0, 1]*100, 4)))
                elif history2[0, 2] > 0.66:
                    self.listWidget.addItem('Capsicum')
                    self.listWidget.addItem(str(round(history2[0, 2]*100, 4)))
                elif history2[0, 3] > 0.66:
                    self.listWidget.addItem('Broccoli')
                    self.listWidget.addItem(str(round(history2[0, 3]*100, 4)))

        else:
            self.listWidget.addItem("No image selected!")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    timer = QtCore.QTimer(MainWindow)
    timer.timeout.connect(lambda: ui.retranslateUi(MainWindow))
    timer.start(1000)
    MainWindow.show()
    sys.exit(app.exec_())

