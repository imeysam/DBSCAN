from Point import Point
from typing import List


class Cluster:
    _status: int
    _points = List[Point]

    def __init__(self):
        self._open = 0
        self._points = []

    def open(self):
        if self._status == 0:
            return True
        else:
            return False

    def status(self, status: int):
        self._status = status

    def addPoint(self, point: Point):
        if point not in self._points:
            self._points.append(point)

    def addPoints(self, points: List[Point]):
        for point in points:
            if point not in self._points:
                self._points.append(point)

    def points(self):
        return self._points
