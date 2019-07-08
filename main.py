from Cluster import Cluster
from Point import Point
import numpy as np
import matplotlib.pyplot as plt

dataset_list = list()

read_file = open('dataset1.txt').readlines()
for row in read_file:
    record = []
    for item in row.split(',')[0].split(';'):
        record.append(int(item) * 10)
    dataset_list.append(record)
dataset = np.array(dataset_list)

epsilon = 75
minPoints = 3

clusters = []

points = []
unvisited_points = []

for data in dataset:
    p = Point(data[0], data[1])
    points.append(p)
    unvisited_points.append(p)

while len(unvisited_points) > 0:
    neighbours = []

    start_point_index = np.random.randint(0, len(unvisited_points))
    start_point = unvisited_points[start_point_index]

    start_point.setVisited(True)
    if start_point in unvisited_points:
        unvisited_points.remove(start_point)

    for point in unvisited_points:
        if abs(point.x() - start_point.x()) <= epsilon and abs(point.y() - start_point.y()) <= epsilon:
            neighbours.append(point)

    if len(neighbours) < minPoints - 1:
        start_point.setNoise(True)
        # for point in neighbours:
        #     point.setNoise(True)
        #     point.setVisited(True)
        #     if point in unvisited_points:
        #         unvisited_points.remove(point)
        neighbours = []
    else:
        cluster = Cluster()
        cluster.addPoints(neighbours)
        cluster.addPoint(start_point)
        clusters.append(cluster)

        while len(neighbours) > 0:
            selected_neighbour = neighbours.pop()
            cluster.addPoint(selected_neighbour)
            selected_neighbour.setVisited(True)
            if selected_neighbour in unvisited_points:
                unvisited_points.remove(selected_neighbour)

            for point_1 in unvisited_points:
                if point_1.getVisited() == False and abs(point_1.x() - selected_neighbour.x()) <= epsilon and abs(
                        point_1.y() - selected_neighbour.y()) <= epsilon:
                    neighbours.append(point_1)

print("Cluster count: {}" . format(len(clusters)))

plt.scatter(dataset[:, 0], dataset[:, 1])
cluster_count = 0
point_count = 0

for cluster in clusters:
    cluster_count += 1
    cluster_points = np.array([[p.x(), p.y()] for p in cluster.points()])
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1])
    for p in cluster.points():
        point_count += 1

    print("Cluster {}th: {}" . format(cluster_count, len(cluster.points())))

print("Noise count: {}" . format(len(dataset) - point_count))

plt.show()
