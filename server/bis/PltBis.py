#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 11:20
# @Author  : cap669
# @File    : PltBis.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout,QLabel,QVBoxLayout
import matplotlib.pyplot as plt
class Widget1(QWidget):

    def __init__(self):
        super().__init__()


class Widget2(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #6666FF;")
        self.label = QLabel("Hello World!")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


class Widget3(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #FFFF66;")
        self.label = QLabel("Hello World!")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

class PltBis(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        grid = QGridLayout()
        self.setLayout(grid)
        self.widget1 = Widget1()
        self.widget2 = Widget2()
        self.widget3 = Widget3()
        grid.addWidget(self.widget1, 0, 0, 2, 1)
        grid.addWidget(self.widget2, 0, 1)
        grid.addWidget(self.widget3, 1, 1)
        self.show()

