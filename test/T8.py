import sys
import matplotlib

matplotlib.use('TkAgg')
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np, math
from pathlib import Path
class Left_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.i =50
        self.j = 50
        self.mod = 0
        self.fig = plt.Figure()
        self.ax: Axes = self.fig.add_subplot()
        self.map = self.Maping()
        self.scan = self.Scaning(self.map.land)
        self.make_plot()
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 1 秒钟更新一次

    class Maping:
        x: int = 200
        y: int = 200
        bn: int = 50

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
            # self.land = self.BuildMap()
            # self.AddBarrier()

        def BuildMap(self):
            return np.zeros((self.x, self.y))

        def AddBarrier(self):
            for i in range(self.bn):
                x, y = np.random.randint(0, self.x, 2)
                xx, yy = np.meshgrid(np.arange(self.x) - x, np.arange(self.x) - y)
                d = np.sqrt(xx ** 2 + yy ** 2)
                self.land[d < 10] = 1

    class Scaning:
        ry = 50

        def __init__(self, land):
            self.land = land

        def RyScan(self, x1, y1):
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
                        e3 = self.land[x1, y1]
                        if e3 == 4:
                            pass
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


    def make_plot(self):
        def func0():
            cmap = plt.cm.colors.ListedColormap(['white', 'blue', 'red', 'aqua'])
            bounds = [0, 1, 2, 3, 4]
            norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

            self.ax.imshow(self.map.land, cmap=cmap, norm=norm, interpolation='nearest')

        def func1():
            pass

        self.__func(func0, func1)

    def update_plot(self):
        # 更新数据
        def func0():
            self.scan.RyScan(self.i, self.j)
            print(self.map.land[self.i, self.j])
            if self.map.land[self.i, self.j] == 1:
                if self.i > 0 and self.j > 0:
                    self.i -= 1
                    self.j -= 1
                else:
                    self.i += 1
            else:
                self.j -= 1
            self.map.land[self.i, self.j] = 4
            self.ax.clear()
            self.make_plot()
            self.canvas.draw()


        def func1():
            pass

        self.__func(func0, func1)

    def __func(self, func0, func1):
        if self.mod == 0:
            func0()
        elif self.mod == 1:
            func1()
        else:
            pass


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 设置窗口的标题和大小
        self.setWindowTitle('PyQt5 Example')
        self.resize(800, 600)

        # 创建一个网格布局，用于放置窗口
        grid = QGridLayout()
        self.setLayout(grid)
        self.showMaximized()
        # 创建左边的2x2窗口
        left_widget = Left_widget()
        left_layout = QGridLayout()
        left_widget.setLayout(left_layout)

        # 创建右边的1x1田字窗口
        right_layout = QHBoxLayout()
        top_layout = QVBoxLayout()
        bottom_layout = QVBoxLayout()

        top_left = QWidget()
        top_left.setStyleSheet('background-color: pink;')
        top_right = QWidget()
        top_right.setStyleSheet('background-color: orange;')
        bottom_left = QWidget()
        bottom_left.setStyleSheet('background-color: gray;')
        bottom_right = QWidget()
        bottom_right.setStyleSheet('background-color: purple;')

        top_layout.addWidget(top_left)
        top_layout.addWidget(top_right)
        bottom_layout.addWidget(bottom_left)
        bottom_layout.addWidget(bottom_right)

        right_layout.addLayout(top_layout)
        right_layout.addLayout(bottom_layout)

        # 将左边和右边的窗口添加到网格布局中
        grid.addWidget(left_widget, 0, 0, 2, 2)
        grid.addLayout(right_layout, 0, 2, 2, 2)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
