# 首页 UI

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainPage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet("QDialog{background: #0099ff}")
        self.weatherTemp = QtWidgets.QLabel(Dialog)
        self.weatherTemp.setGeometry(QtCore.QRect(520, 80, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.weatherTemp.setFont(font)
        self.weatherTemp.setText("")
        self.weatherTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weatherTemp.setObjectName("weatherTemp")
        self.weatherText = QtWidgets.QLabel(Dialog)
        self.weatherText.setGeometry(QtCore.QRect(520, 60, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.weatherText.setFont(font)
        self.weatherText.setText("")
        self.weatherText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weatherText.setObjectName("weatherText")
        self.weatherIcon = QtWidgets.QLabel(Dialog)
        self.weatherIcon.setGeometry(QtCore.QRect(497, 10, 51, 51))
        self.weatherIcon.setStyleSheet("QLabel{background:white;}")
        self.weatherIcon.setText("")
        self.weatherIcon.setObjectName("weatherIcon")
        self.locaName = QtWidgets.QLabel(Dialog)
        self.locaName.setGeometry(QtCore.QRect(557, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.locaName.setFont(font)
        self.locaName.setObjectName("locaName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(17, 30, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.locaName.setText(_translate("Dialog", "杭州"))
        self.label_2.setText(_translate("Dialog", "今天共有 3 节课"))

    def setWeatherIcon(self, iconID):
        self.weatherIcon.setStyleSheet("QLabel{border-image: url(assets/weatherIcon/" + iconID + ".png); }")