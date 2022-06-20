from _Attitude import Attitude
from _Position import Position


class Vehicle:
    def __init__(self):
        self.attitude = Attitude()
        self.position = Position()


class Copter(Vehicle):
    def __init__(self):
        super().__init__()


class Plane(Vehicle):
    def __init__(self):
        super().__init__()
