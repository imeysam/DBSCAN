from Cluster import Cluster
from Point import Point
import numpy as np
import math
from sklearn import datasets


def removeNeighbour(item):
    if item in neighbours:
        neighbours.remove(item)


def removePoint(item, list):
    if item in list:
        unvisited_points.remove(item)


def distance(first, second):
    return math.sqrt(
        ((first.x() - second.x()) ** 2) +
        ((first.y() - second.y()) ** 2) +
        ((first.z() - second.z()) ** 2) +
        ((first.o() - second.o()) ** 2)
    )


dataset_list = list()

"""
Read dataset from text file
"""
# read_file = open('iris.data').readlines()
# for row in read_file:
#     record = []
#     for item in row.split(','):
#         if len(item) == 3 or len(item) == 4:
#             record.append(float(item))
#     if len(record) == 4:
#         dataset_list.append(record)
# dataset = np.array(dataset_list)

iris = datasets.load_iris()
dataset = iris.data

epsilon = 0.39
minPoints = 4

clusters = []

"""List of points"""
points = []
unvisited_points = []
noise_points = []

"""
Convert dataset to objects
"""
for data in dataset:
    p = Point(data[0], data[1], data[2], data[3])
    points.append(p)
    unvisited_points.append(p)

while len(unvisited_points) > 0:
    neighbours = []

    """Select Random start point"""
    start_point_index = np.random.randint(0, len(unvisited_points))
    start_point = unvisited_points[start_point_index]

    start_point.setVisited(True)
    if start_point in unvisited_points:
        unvisited_points.remove(start_point)

    """Find start point neighbourhoods"""
    for point in points:
        if distance(point, start_point) <= epsilon:
            neighbours.append(point)

    removeNeighbour(start_point)

    """Check if neighbours less than min points"""
    if len(neighbours) < minPoints:
        noise_points.append(start_point)
        removePoint(start_point, unvisited_points)

    else:
        """Else if neighbours equal or more than min points"""

        """Make a new cluster"""
        cluster = Cluster()

        """Add neighbours to created cluster"""
        cluster.addPoints(neighbours)
        cluster.addPoint(start_point)
        clusters.append(cluster)

        """Check all neighbours from selected start point"""
        while len(neighbours) > 0:
            """Pop a neighbour"""
            selected_neighbour = neighbours.pop()

            """Add selected neighbour to cluster"""
            cluster.addPoint(selected_neighbour)

            removePoint(selected_neighbour, unvisited_points)
            selected_neighbour.setVisited(True)

            """Find all neighbours of was pop neighbour"""
            for point_1 in points:
                if point_1.getVisited() == False and distance(point_1, selected_neighbour) <= epsilon:
                    neighbours.append(point_1)

print("Cluster count: {}" . format(len(clusters)))

cluster_count = 0

rates = []

"""Plot all data on a page"""
for cluster in clusters:
    cluster_count += 1
    print("Cluster {}th: {}" . format(cluster_count, len(cluster.points())))
    rates.append(len(cluster.points()))

print("Noise count: {}" . format(len(noise_points)))


rate = ((sum(rates) * 2) / (len(clusters)))
print('Rate: {}%' . format(rate))

