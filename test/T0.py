import matplotlib
matplotlib.use('TkAgg')
import random
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# 定义地图大小和起点终点位置
map_size = (200, 200)
start = (0, 0)
end = (199, 199)

# 定义地图数组，0表示可通行区域，1表示障碍物区域
map = np.zeros(map_size)

# 随机添加圆形障碍物
for i in range(50):
    x = random.randint(20, map_size[0] - 20)
    y = random.randint(20, map_size[1] - 20)
    r = random.randint(5, 20)
    for j in range(map_size[0]):
        for k in range(map_size[1]):
            if sqrt((j - x) ** 2 + (k - y) ** 2) <= r:
                map[j, k] = 1


# 定义启发式函数，使用曼哈顿距离
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# 定义 A* 寻路算法
def astar_search(map, start, end):
    open_set = set([start])
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_set.remove(current)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if not (0 <= neighbor[0] < map.shape[0]) or not (0 <= neighbor[1] < map.shape[1]):
                continue
            if map[neighbor[0], neighbor[1]] == 1:
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                if neighbor not in open_set:
                    open_set.add(neighbor)


# 动态可视化
fig, ax = plt.subplots()
ax.imshow(map, cmap=plt.cm.Dark2)

path = astar_search(map, start, end)
print(len(path))
for i in range(len(path) - 1):
    ax.plot((path[i][1], path[i + 1][1]), (path[i][0], path[i + 1][0]), color='blue')
    plt.pause(0.01)

plt.show()
