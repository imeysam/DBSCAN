from DBSCAN import DBSCAN
from Cluster import Cluster
from Point import Point
import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([
    # classter 1
    [26, 25],
    [34, 23],
    [25, 23],
    [28, 11],
    [30, 15],
    [31, 19],
    [27, 12],
    [36, 11],
    [37, 24],
    [34, 18],

    # claster2
    [66, 10],
    [67, 30],
    [66, 31],
    [67, 23],
    [70, 28],
    [65, 11],
    [72, 18],
    [69, 19],
    [69, 15],
    [74, 26],
    [71, 29],
    [68, 21],
    [66, 31],
    [73, 9],
    [67, 17],

    # claster3
    [50, 60],
    [51, 80],
    [46, 74],
    [55, 55],
    [60, 67],
    [48, 68],
    [47, 78],
    [56, 66],
    [52, 77],
    [58, 60],
    [49, 80],
    [57, 79],
    [50, 65],
    [49, 68],
    [59, 73],
    [60, 71],
    [47, 61],
    [47, 65],
    [51, 76],
    [50, 77],
    [58, 74],
    [57, 63],
    [56, 69],
    [46, 68],
    [47, 60],

    # noise
    [25, 70],
    [25, 50],
    [50, 10],
    [44, 42],
    [42, 42],

])

noise = np.array([
    [25, 70],
    [25, 50],
    [50, 10],
    [44, 42],
    [42, 42],
])

epsilon = 10
minPoints = 3

clusters = []

points = []
for data in dataset:
    points.append(Point(data[0], data[1]))

# start_point_index = np.random.randint(0, len(points))
start_point_index = 52
start_point = points[start_point_index]

print(start_point, start_point_index)
print(points[42])
print(points[42])

neighbours = []

# for point in points:
#     point.setVisited(True)
#     if abs(point.x() - start_point.x()) <= epsilon and abs(point.y() - start_point.y()) <= epsilon:
#         neighbours.append(point)

for point in points:
    if abs(point.x() - start_point.x()) <= epsilon and abs(point.y() - start_point.y()) <= epsilon:
        neighbours.append(point)


if len(neighbours) < minPoints:
    for point in neighbours:
        point.setNoise(True)
        point.setVisited(True)
    neighbours = []
else:
    cluster = Cluster()
    cluster.addPoints(neighbours)
    clusters.append(cluster)

    while len(neighbours) > 1:
        selected_neighbour = neighbours.pop()
        cluster.addPoint(selected_neighbour)
        selected_neighbour.setVisited(True)

        for point_1 in points:
            if point_1.getVisited() == False and abs(point_1.x() - selected_neighbour.x()) <= epsilon and abs(
                    point_1.y() - selected_neighbour.y()) <= epsilon:
                neighbours.append(point_1)
                # cluster.addPoint(point_1)

print(len(clusters))
# plt.scatter(dataset[:, 0], dataset[:, 1])
# plt.scatter(noise[:, 0], noise[:, 1])
# plt.show()
