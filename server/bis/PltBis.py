#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 11:20
# @Author  : cap669
# @File    : PltBis.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout,QLabel,QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np,math
from random import choice
from matplotlib.animation import FuncAnimation
class Widget1(QWidget):

    def __init__(self,data):
        super().__init__()
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot()
        self.ax.imshow(data)
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)


mngles = []
class Widget2(QWidget):

    def __init__(self,get_circle_image):
        super().__init__()
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot()
        img = get_circle_image(100,100,50)
        img[50, 50] = 2
        self.scan(img)
        self.ax.imshow(img)
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def scan(self,img):

        # 激光雷达位置
        laser_pos = np.array([50, 50])
        # 激光雷达最大探测距离
        max_range = 20
        # 扫描的角度范围
        angles = np.linspace(0, 2 * np.pi, 360, endpoint=False)

        # 存储扫描结果的数组
        lidar_scan = np.zeros(360)

        # 对每个角度进行扫描
        for i, angle in enumerate(angles):
            # 计算扫描线的结束点
            end_pos = laser_pos + max_range * np.array([np.cos(angle), -np.sin(angle)])
            # 在扫描线上均匀采样
            samples = np.linspace(laser_pos, end_pos, num=100)
            # 遍历每个采样点，寻找最近障碍物
            for sample in samples:
                x, y = sample.astype(int)
                # 如果当前采样点已经超出图像范围，停止本次扫描
                if x < 0 or x >= img.shape[0] or y < 0 or y >= img.shape[1]:
                    break
                # 如果当前采样点对应的像素值不为0，表示扫描到了障碍物，记录距离并停止本次扫描
                if img[x, y] != 0:
                    lidar_scan[i] = np.linalg.norm(sample - laser_pos)
                    break
        global mngles
        mngles = list(angles)

class Widget3(QWidget):
    def __init__(self,data):
        super().__init__()
        self.fig = plt.Figure()
        self.ax:Axes = self.fig.add_subplot(projection='polar')
        theta = np.array([0.25, 0.75, 1, 1.5, 0.25])
        r = [20, 60, 40, 80, 20]
        self.ax.plot(theta*np.pi, r, color='red', linewidth=1)
        # self.ax.fill(theta, r, 'm', alpha=0.75)
        # self.ax.set_rmax(100)
        # self.ax.set_rticks([20, 40, 60, 80, 100])
        # self.ax.set_rlabel_position(0)
        # self.ax.grid(True)
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
class PltBis(QWidget):
    def __init__(self,data,get_circle_image):
        super().__init__()
        self.showMaximized()
        grid = QGridLayout()
        self.setLayout(grid)
        self.widget1 = Widget1(data)
        self.widget2 = Widget2(get_circle_image)
        self.widget3 = Widget3(data)
        grid.addWidget(self.widget1, 0, 0, 2, 1)
        grid.addWidget(self.widget2, 0, 1)
        grid.addWidget(self.widget3, 1, 1)
        self.show()

