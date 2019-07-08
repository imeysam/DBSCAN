from Point import Point
from Cluster import Cluster
from typing import List
import math
import numpy as np


class DBSCAN:
    """
    Simple implementation of DBSCAN algorithm
    """

    _epsilon: float
    _minPoints: int
    _unvisitedPoints: List[Point]
    _noisePoints: List[Point]
    _points: List[Point]
    _neighbours: List[Point]
    _clusters: List[Cluster]

    def __init__(self, dataset, epsilon: float, min_points: int):
        self._dataset = dataset
        self._epsilon = epsilon
        self._minPoints = min_points
        self._points = []
        self._unvisitedPoints = []
        self._neighbours = []
        self._noisePoints = []
        self._clusters = []
        self.fillData()

    def removeNeighbours(self, point: Point):
        """Remove the point from neighbourhoods list"""
        if point in self._neighbours:
            self._neighbours.remove(point)

    def removePoint(self, point: Point):
        """Remove a visited point from unvisited points list"""
        if point in self._unvisitedPoints:
            self._unvisitedPoints.remove(point)

    def getPoints(self):
        """
        Get list of all points (visited and unvisited)
        """
        return self._points

    def run(self):
        """Run algorithm"""

        """Select Random start point"""
        start_point = self.randomSelect()
        start_point.setVisited(True)
        self.removePoint(start_point)

        """Find start point neighbourhoods"""
        for point in self._points:
            if self.distance(point, start_point) <= self._epsilon:
                self._neighbours.append(point)

        self.removeNeighbours(start_point)

        """Check if neighbours less than min points"""
        if len(self._neighbours) < self._minPoints:
            self._noisePoints.append(start_point)
            self.removePoint(start_point)
        else:
            """Else if neighbours equal or more than min points"""

            """Make a new cluster"""
            cluster = Cluster()

            """Add neighbours to created cluster"""
            cluster.addPoints(self._neighbours)
            cluster.addPoint(start_point)
            self._clusters.append(cluster)

            """Check all neighbours from selected start point"""
            while len(self._neighbours) > 0:
                """Pop a neighbour"""
                selected_neighbour = self._neighbours.pop()

                """Add selected neighbour to cluster"""
                cluster.addPoint(selected_neighbour)

                self.removePoint(selected_neighbour)
                selected_neighbour.setVisited(True)

                """Find all neighbours of was pop neighbour"""
                for point_1 in self._points:
                    if point_1.getVisited() == False and self.distance(point_1, selected_neighbour) <= self._epsilon:
                        self._neighbours.append(point_1)
        return self

    def rate(self):
        pass


    def getClusters(self):
        """
        Get list of cluster
        After call run() method
        """
        return self._clusters

    def getNoise(self):
        """
        Get list of noise
        After call run() method
        """
        return self._noisePoints

    @staticmethod
    def distance(first_point: Point, second_point: Point):
        """Calculate Euclidean distance between 2 points by 4 features"""
        return math.sqrt(
            ((first_point.x() - second_point.x()) ** 2) +
            ((first_point.y() - second_point.y()) ** 2) +
            ((first_point.z() - second_point.z()) ** 2) +
            ((first_point.o() - second_point.o()) ** 2)
        )

    def randomSelect(self):
        start_point_index = np.random.randint(0, len(self._unvisitedPoints))
        return self._unvisitedPoints[start_point_index]

    def fillData(self):
        dataset = self._dataset
        print(dataset)
        for data in dataset:
            temp_point = Point(data[0], data[1], data[2], data[3])
            self._points.append(temp_point)
            self._unvisitedPoints.append(temp_point)
