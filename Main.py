# Kagami 入口

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# 加载 UI
import MainpageUI

# 获取天气信息



# PyQt 窗体设置
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = MainpageUI.Ui_MainPage()   # 设置首页结款
ui.setupUi(Dialog)
Dialog.show()   # 显示首页

sys.exit(app.exec_())