#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 22:14
# @Author  : cap669
# @File    : T2.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

class T2:
    def __init__(self):
        self.map = self.Maping()
        self.scan = self.Scaning(self.map.land)
        # for s in range(50,150,10):
        #     self.scan.RyScan(50, s)
        #     break

        self.Showing(self.map.land)

    class Maping:
        x:int = 200
        y:int = 200
        bn:int = 20
        def __init__(self):
            self.land = None
            p = Path('a.npy')
            g = p.__str__()
            if p.exists():
                self.land = np.load(g)
            else:
                self.land = self.BuildMap()
                self.AddBarrier()
                np.save(g, self.land)
        def BuildMap(self):
            return np.zeros((self.x, self.y))
        def AddBarrier(self):
            for i in range(self.bn):
                x, y = np.random.randint(0, self.x, 2)
                xx, yy = np.meshgrid(np.arange(self.x) - x, np.arange(self.x) - y)
                d = np.sqrt(xx ** 2 + yy ** 2)
                self.land[d < 5] = 1

    class Scaning:
        ry = 50
        def __init__(self,land):
            self.land = land
        def RyScan(self,x1, y1):
            def func0(x1, y1):
                dx = np.cos(np.deg2rad(i))
                dy = np.sin(np.deg2rad(i))
                # 使用布雷斯汉姆直线演算法做360次扫描
                x2, y2 = int(x1 + self.ry * dx), int(y1 + self.ry * dy)
                dx, dy = x2 - x1, y2 - y1
                sx, sy = np.sign(dx), np.sign(dy)
                dx, dy = abs(dx), abs(dy)
                err = dx - dy

                while x1 != x2 or y1 != y2:
                    if self.land[x1, y1] == 1:
                        # self.land[x1, y1] = 3  # 将障碍物的像素值改为红色
                        break
                    else:
                        self.land[x1, y1] = 2
                    e2 = 2 * err
                    if e2 > -dy:
                        err -= dy
                        x1 += sx
                    if e2 < dx:
                        err += dx
                        y1 += sy

                # 在地图上绘制扫描结果
                # self.land[x1, y1] = 2
            for i in range(360):
               func0(x1, y1)
    class Showing:
        def __init__(self,land):
            cmap = plt.cm.colors.ListedColormap(['white', 'blue', 'red'])
            bounds = [0, 1, 2, 3]
            norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

            # 显示地图
            plt.imshow(land, cmap=cmap, norm=norm, interpolation='nearest')
            plt.show()
if __name__ == '__main__':
    T2()
