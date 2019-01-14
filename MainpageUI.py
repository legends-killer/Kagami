# -*- coding: UTF-8 -*-

# 首页 UI

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_MainPage(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 768)
        Dialog.setStyleSheet("QDialog{background-image: url(assets/background/01.jpg); background-position:center;}")

        self.weatherTemp = QtWidgets.QLabel(Dialog)
        self.weatherTemp.setGeometry(QtCore.QRect(855, 105, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.weatherTemp.setFont(font)
        self.weatherTemp.setText("")
        self.weatherTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weatherTemp.setObjectName("weatherTemp")
        self.weatherTemp.setStyleSheet("QLabel{color:white;}")

        self.weatherText = QtWidgets.QLabel(Dialog)
        self.weatherText.setGeometry(QtCore.QRect(655, 150, 350, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.weatherText.setFont(font)
        self.weatherText.setText("")
        self.weatherText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weatherText.setObjectName("weatherText")
        self.weatherText.setStyleSheet("QLabel{color:white;}")

        self.weatherIcon = QtWidgets.QLabel(Dialog)
        self.weatherIcon.setGeometry(QtCore.QRect(760, 25, 120, 120))
        self.weatherIcon.setStyleSheet("QLabel{background:white;}")
        self.weatherIcon.setText("")
        self.weatherIcon.setObjectName("weatherIcon")

        self.locaName = QtWidgets.QLabel(Dialog)
        self.locaName.setGeometry(QtCore.QRect(860, 25, 150, 100))
        self.locaName.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(55)
        self.locaName.setFont(font)
        self.locaName.setObjectName("locaName")
        self.locaName.setStyleSheet("QLabel{color:white;}")

        # 一卡通余额卡片
        self.yktCard = QtWidgets.QLabel(Dialog)
        self.yktCard.setGeometry(QtCore.QRect(10, 10, 350, 220))
        self.yktCard.setText("")
        self.yktCard.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft)
        self.yktCard.setObjectName("yktCard")
        self.yktCard.setStyleSheet("QLabel{background-image: url(assets/card/yikatong.png);}")

        # 一卡通余额
        self.yktBalance = QtWidgets.QLabel(Dialog)
        self.yktBalance.setGeometry(QtCore.QRect(200, 23, 120, 60))
        self.yktBalance.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft)
        self.yktBalance.setObjectName("yktBalance")
        self.yktBalance.setText("")
        self.yktBalance.setStyleSheet("QLabel{color:rgba(255,255,255,0.8); font-size:32px;}")

        # 一卡通今日花费
        self.yktToday = QtWidgets.QLabel(Dialog)
        self.yktToday.setGeometry(QtCore.QRect(200, 93, 120, 60))
        self.yktToday.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft)
        self.yktToday.setObjectName("yktToday")
        self.yktToday.setText("")
        self.yktToday.setStyleSheet("QLabel{color:rgba(255,255,255,0.8); font-size:32px;}")

        # 宿舍电费
        self.powerRate = QtWidgets.QLabel(Dialog)
        self.powerRate.setGeometry(QtCore.QRect(200, 163, 120, 60))
        self.powerRate.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft)
        self.powerRate.setObjectName("powerRate")
        self.powerRate.setText("")
        self.powerRate.setStyleSheet("QLabel{color:rgba(255,255,255,0.8); font-size:32px;}")

        # 时间
        self.timeText = QtWidgets.QLabel(Dialog)
        self.timeText.setGeometry(QtCore.QRect(450, 280, 550, 110))
        self.timeText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeText.setObjectName("timeText")
        self.timeText.setText("")
        self.timeText.setStyleSheet("QLabel{color:white; font-size:130px;}")

        # 日期
        self.dateText = QtWidgets.QLabel(Dialog)
        self.dateText.setGeometry(QtCore.QRect(600, 400, 400, 40))
        self.dateText.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dateText.setObjectName("dateText")
        self.dateText.setText("")
        self.dateText.setStyleSheet("QLabel{color:white; font-size:32px;}")

        # 上课信息
        self.classSummary = QtWidgets.QLabel(Dialog)
        self.classSummary.setGeometry(QtCore.QRect(20, 230, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.classSummary.setFont(font)
        self.classSummary.setStyleSheet("QLabel{color:white;}")
        self.classSummary.setObjectName("classSummary")

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Tag
        self.tag = QtWidgets.QLabel(Dialog)
        self.tag.setGeometry(QtCore.QRect(700, 500, 300, 250))
        self.tag.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeft)
        self.tag.setObjectName("tag_1")
        self.tag.setWordWrap(True)
        self.tag.setText("这里是已经留出了 API 接口的备忘信息。我可以用手机输入信息然后投到上面。")
        self.tag.setStyleSheet("QLabel{color:white; font-size:25px; background-color:rgba(0,0,0,0.5); padding:10px}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kagami"))   # 窗体标题
        self.locaName.setText(_translate("Dialog", "杭州"))

        self.classSummary.setText(_translate("Dialog", ""))


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

    # 设置一卡通余额
    def setCard(self, remaining, today):
        self.yktBalance.setText(str(remaining) + " 元")
        self.yktToday.setText(str(today) + " 元")

    # 设置电费
    def setPowerRate(self, powerRate):
        self.powerRate.setText(str(powerRate) + " 元")

    # 更新时间
    def updateTime(self):
        self.timeText.setText(str(time.strftime('%H:%M:%S', time.localtime(time.time()))))

    # 更新日期
    def updateDate(self):
        week = ['天', '一', '二', '三', '四', '五', '六']
        date = str(time.strftime('%Y年%m月%d日 ', time.localtime(time.time())))
        date += "星期" + week[int(time.strftime('%w', time.localtime(time.time())))]
        self.dateText.setText(date)
