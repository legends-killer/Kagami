# 首页 UI

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainPage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet("QDialog{background-image: url(assets/background/01.jpg); background-position:center;}")

        self.weatherTemp = QtWidgets.QLabel(Dialog)
        self.weatherTemp.setGeometry(QtCore.QRect(520, 80, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.weatherTemp.setFont(font)
        self.weatherTemp.setText("")
        self.weatherTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weatherTemp.setObjectName("weatherTemp")
        self.weatherTemp.setStyleSheet("QLabel{color:white;}")

        self.weatherText = QtWidgets.QLabel(Dialog)
        self.weatherText.setGeometry(QtCore.QRect(460, 55, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.weatherText.setFont(font)
        self.weatherText.setText("")
        self.weatherText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weatherText.setObjectName("weatherText")
        self.weatherText.setStyleSheet("QLabel{color:white;}")

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
        self.locaName.setStyleSheet("QLabel{color:white;}")

        # 一卡通余额卡片
        self.yktCard = QtWidgets.QLabel(Dialog)
        self.yktCard.setGeometry(QtCore.QRect(10, 10, 200, 90))
        self.yktCard.setText("")
        self.yktCard.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yktCard.setObjectName("yktCard")
        self.yktCard.setStyleSheet("QLabel{background-image: url(assets/card/yikatong.png);}")

        # 一卡通余额
        self.yktBalance = QtWidgets.QLabel(Dialog)
        self.yktBalance.setGeometry(QtCore.QRect(10, 10, 200, 90))
        self.yktBalance.setText("10 元")
        self.yktBalance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yktBalance.setObjectName("yktBalance")
        self.yktBalance.setStyleSheet("QLabel{color:white; font-size:30px;}")


        self.classSummary = QtWidgets.QLabel(Dialog)
        self.classSummary.setGeometry(QtCore.QRect(17, 30, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.classSummary.setFont(font)
        self.classSummary.setStyleSheet("QLabel{color:white;}")
        self.classSummary.setObjectName("classSummary")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kagami"))   # 窗体标题
        self.locaName.setText(_translate("Dialog", "杭州"))

        self.classSummary.setText(_translate("Dialog", "今天共有 3 节课"))

    # 设置天气图标
    def setWeatherIcon(self, iconID):
        self.weatherIcon.setStyleSheet("QLabel{border-image: url(assets/weatherIcon/" + iconID + ".png); }")

    # 设置天气状态
    def setWeatherStatus(self, status):
        self.weatherText.setText(status)

    # 设置天气温度
    def setWeatherTemp(self, min, max):
        self.weatherTemp.setText(str(min) + " ℃ - " + str(max) + " ℃")

    # 设置课表文字总结
    def setClassSummary(self, summaryText):
        self.classSummary.setText(summaryText)

