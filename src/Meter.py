# -*- coding:utf-8 -*-
# 导入 demo02_ui
from LaserMeter import *
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

# 继承 Ui_MainWindow类


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())