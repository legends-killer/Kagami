# Kagami 入口

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
from urllib import parse, request

import Config
# 加载 UI
import MainpageUI

# PyQt 窗体设置
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = MainpageUI.Ui_MainPage()   # 设置首页结款
ui.setupUi(Dialog)


Dialog.show()   # 显示首页


def get_info_stream():
    url = "https://api.hduhelp.com/infoStream/v3"
    req = request.Request(url = url)
    req.add_header('User-Agent', 'Raspberry Pi')
    req.add_header('Authorization', 'token 00dWyA39onl8pboMgyx5jveSv0BtD6g4Zo9mYzZ')
    req.add_header('Referer', 'https://app.hduhelp.com/')
    req.add_header('Origin', 'https://app.hduhelp.com/')

    response = request.urlopen(req)
    response = response.read()
    response = json.loads(response)

    return response


infoStream = get_info_stream()


# 获取天气信息
def set_weather_data():

    weatherIcon = infoStream['data']['weather']['data']['skyconNow']
    weatherStatus = infoStream['data']['weather']['data']['desc']
    weatherTempMin = infoStream['data']['weather']['data']['temperatureMin']
    weatherTempMax = infoStream['data']['weather']['data']['temperatureMax']

    ui.setWeatherIcon(weatherIcon)  # 设置天气图标
    ui.setWeatherStatus(weatherStatus)
    ui.setWeatherTemp(weatherTempMin, weatherTempMax)


set_weather_data()




# 获取课表信息
def set_class_data():
    todayCount = infoStream['data']['schedule']['data']['today']
    tomorrowCount = infoStream['data']['schedule']['data']['tomorrow']

    if len(todayCount) == 0:
        summaryText = "今天没有课！开心！"
    else:
        summaryText = "今天你有" + todayCount + "节课"

    ui.setClassSummary(summaryText)


#set_class_data()


# 获取一卡通信息
def set_ykt():
    remaining = infoStream['data']['card']['data']['remaining']
    today = infoStream['data']['card']['data']['today']

    ui.setCard(remaining, today)


set_ykt()

# TODO:按照返回的数据调用函数
#for item in infoStream['data']['_sort']:


sys.exit(app.exec_())