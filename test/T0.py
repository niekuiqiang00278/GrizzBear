import numpy as np
import matplotlib.pyplot as plt

# 生成100x100的2D地图
map = np.zeros((200, 200))

# 随机生成5个10x10圆形
for i in range(20):
    x, y = np.random.randint(0, 200, 2)
    xx, yy = np.meshgrid(np.arange(200) - x, np.arange(200) - y)
    d = np.sqrt(xx ** 2 + yy ** 2)
    map[d < 5] = 1

# 计算每个扫描点的坐标
x = np.linspace(-50, 50, 360)
y = np.zeros(360)

# 生成雷达地图
for i in range(360):
    dx = np.cos(np.deg2rad(i))
    dy = np.sin(np.deg2rad(i))

    # 使用布雷斯汉姆直线演算法做360次扫描
    x1, y1 = 50, 50
    x2, y2 = int(x1 + 50 * dx), int(y1 + 50 * dy)
    dx, dy = x2 - x1, y2 - y1
    sx, sy = np.sign(dx), np.sign(dy)
    dx, dy = abs(dx), abs(dy)
    err = dx - dy

    while x1 != x2 or y1 != y2:
        if map[x1, y1] == 1:
            map[x1, y1] = 3 # 将障碍物的像素值改为红色
            break
        else:
            map[x1, y1] = 2
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    # 在地图上绘制扫描结果
    map[x1, y1] = 2

# 设置颜色映射
cmap = plt.cm.colors.ListedColormap(['white', 'blue', 'red'])
bounds = [0, 1, 2, 3]
norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

# 显示地图
plt.imshow(map, cmap=cmap, norm=norm, interpolation='nearest')
plt.show()
