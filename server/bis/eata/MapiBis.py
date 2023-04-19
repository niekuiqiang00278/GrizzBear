#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 12:20
# @Author  : cap669
# @File    : MapiBis.py
# @Software: PyCharm
import numpy as np
import random
import math,cv2
class MapiBis:
    h: int = 500
    w: int = 500

    def __init__(self):
        self.crust = self.make_crust()
        for s in range(50):
            self.add_circle()
            self.add_square()
            self.add_triangle()

    def get_circle_image(self, x, y, r):
        mask = np.zeros((self.w, self.h), dtype=np.uint8)
        cv2.circle(mask, (x, y), r, 1, -1)
        img = self.crust[y - r:y + r, x - r:x + r]
        return img
    def make_crust(self):
        return np.zeros((self.w, self.h))

    def add_circle(self):
        x, y = np.random.randint(0, self.h, 2)
        r = np.random.randint(5, 10)
        xx, yy = np.meshgrid(np.arange(self.w), np.arange(self.h))
        dist = np.sqrt((xx - x) ** 2 + (yy - y) ** 2)
        self.crust[dist < r] = 1

    def add_square(self):
        size = random.randint(5, 10)
        x, y = np.random.randint(size, self.w - size, 2)
        self.crust[x - size:x + size, y - size:y + size] = 1

    def add_triangle(self):
        x1, y1 = np.random.randint(0, self.h, 2)
        side = np.random.randint(10, 20)
        height = side * math.sqrt(3) / 2
        x2, y2 = x1 + side, y1
        x3, y3 = x1 + side / 2, y1 + height
        xx, yy = np.meshgrid(np.arange(self.w), np.arange(self.h))
        A = (x1, y1)
        B = (x2, y2)
        C = (x3, y3)
        AB = (B[0] - A[0], B[1] - A[1])
        AC = (C[0] - A[0], C[1] - A[1])
        BC = (C[0] - B[0], C[1] - B[1])
        BA = (A[0] - B[0], A[1] - B[1])
        CA = (A[0] - C[0], A[1] - C[1])
        CB = (B[0] - C[0], B[1] - C[1])
        s1 = np.sign(AB[0] * yy - AB[1] * xx + B[1] * A[0] - B[0] * A[1])
        s2 = np.sign(BC[0] * yy - BC[1] * xx + C[1] * B[0] - C[0] * B[1])
        s3 = np.sign(CA[0] * yy - CA[1] * xx + A[1] * C[0] - A[0] * C[1])
        self.crust[(s1 == s2) & (s2 == s3)] = 1