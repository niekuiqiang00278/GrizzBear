#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 12:20
# @Author  : cap669
# @File    : MapiBis.py
# @Software: PyCharm
import numpy as np
class MapiBis:
    h: int = 200
    w: int = 200

    def __init__(self):
        self.crust = self.make_crust()
        self.add_circle()

    def make_crust(self):
        return np.zeros((self.w, self.h))

    def add_circle(self):
        x, y = np.random.randint(0, self.h, 2)
        r = np.random.randint(5, 10)
        xx, yy = np.meshgrid(np.arange(self.w), np.arange(self.h))
        dist = np.sqrt((xx - x) ** 2 + (yy - y) ** 2)
        self.crust[dist < r] = 1
