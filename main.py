from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

import numpy as np
import keras


import keras.preprocessing
from keras.models import load_model




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(700, 380)
        MainWindow.setFixedWidth(700)
        MainWindow.setFixedHeight(380)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TakePhotoButton = QtWidgets.QPushButton(self.centralwidget)
        self.TakePhotoButton.setGeometry(QtCore.QRect(40, 300, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.TakePhotoButton.setFont(font)
        self.TakePhotoButton.setMouseTracking(False)
        self.TakePhotoButton.setStyleSheet("QPushButton#TakePhotoButton:hover{		\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"border-style: double;\n"
"border-width: 3px 3px 3px 3px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#TakePhotoButton:!hover{\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);\n"
"border-style: double;\n"
"border-width: 3px 3px 3px 3px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.TakePhotoButton.setObjectName("TakePhotoButton")
        self.TextLabel = QtWidgets.QLabel(self.centralwidget)
        self.TextLabel.setGeometry(QtCore.QRect(370, 300, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.TextLabel.setFont(font)
        self.TextLabel.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);\n"
"border-style: double;\n"
"border-width: 3px 3px 3px 3px;\n"
"color:rgb(255, 255, 255);\n"
"text-align: center;")
        self.TextLabel.setObjectName("LabelProbability")
        self.ThePhoto = QtWidgets.QLabel(self.centralwidget)
        self.ThePhoto.setGeometry(QtCore.QRect(40, 20, 250, 250))
        self.ThePhoto.setStyleSheet("")
        self.ThePhoto.setText("")
        self.ThePhoto.setObjectName("ThePhoto")
        self.Probability = QtWidgets.QLabel(self.centralwidget)
        self.Probability.setGeometry(QtCore.QRect(500, 300, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Probability.setFont(font)
        self.Probability.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);\n"
"border-style: double;\n"
"border-width: 3px 3px 3px 3px;\n"
"color:rgb(255, 255, 255);\n"
"text-align: center;")
        self.Probability.setText("")
        self.Probability.setObjectName("Probability")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пневмония"))
        self.TakePhotoButton.setText(_translate("MainWindow", "Выбрать фото"))
        self.TextLabel.setText(_translate("MainWindow", "Вероятность"))

    def CalculateProbability(self,pathToPhoto):
        image = keras.preprocessing.image.load_img(pathToPhoto,
                                                   target_size=(150, 150), color_mode='rgb', interpolation='nearest')
        input_arr = keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])
        input_arr /= 255
        predictions = self.myModel.predict(input_arr)
        return round(100*predictions[0][0],2)

    def OpenPhoto(self):
        file, _ = QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        #self.ThePhoto.setStyleSheet("background-image: url("+file+"); background-size: contain;")
        if file!='':
            pixFile=QPixmap(file)
            pixFile=pixFile.scaled(250,250)
            self.ThePhoto.setPixmap(pixFile)
            self.Probability.setText(str(self.CalculateProbability(file)))


    def Connection(self):
        self.myModel = load_model('TheModel')
        self.TakePhotoButton.clicked.connect(self.OpenPhoto)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Connection()
    MainWindow.show()
    sys.exit(app.exec_())
