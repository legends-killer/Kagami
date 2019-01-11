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


# 获取天气信息
def get_weather_data():
    url = "https://api.seniverse.com/v3/weather/now.json?key=" + Config.weatherKey + "&location=hangzhou&language=zh-Hans&unit=c"
    req = request.Request(url = url)
    response = request.urlopen(req)
    response = response.read()
    response = json.loads(response)

    weatherStatus = response['results'][0]['now']['text']
    weatherIcon = response['results'][0]['now']['code']
    weatherTemp = response['results'][0]['now']['temperature']

    ui.setWeatherIcon(weatherIcon)  # 设置天气图标

get_weather_data()


Dialog.show()   # 显示首页
sys.exit(app.exec_())