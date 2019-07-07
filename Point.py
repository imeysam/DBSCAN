class Point:
    _x: int
    _y: int
    _type: int
    _visited: bool
    _finished: bool
    _noise: bool

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._visited = False
        self._type = 0
        self._finished = False
        self._noise = False

    def __repr__(self):
        return "P[{} {}]" . format(self.x(), self.y())

    def x(self):
        return self._x

    def y(self):
        return self._y

    def getVisited(self):
        return self._visited

    def setVisited(self, visited: bool):
        self._visited = visited

    def type(self, type: int):
        self._type = type

    def type(self) -> int:
        return self._type

    def finished(self, finished: bool):
        self._finished = finished

    def finished(self) -> bool:
        return self._finished

    def setNoise(self, noise: bool):
        self._noise = noise

    def getNoise(self) -> bool:
        return self._noise
