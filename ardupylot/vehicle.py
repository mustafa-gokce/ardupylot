from ardupylot._Attitude import Attitude
from ardupylot._Position import Position
import ardupylot._Exception as _Exception


class Vehicle:
    def __init__(self, connection_string=None, connect_now=False):
        self.connection_string = connection_string
        self.connect_now = connect_now
        self._connected = False
        self.attitude = Attitude()
        self.position = Position()

        if self.connect_now:
            self.connect()

    @property
    def connected(self):
        return self._connected

    def connect(self):
        if self.connected:
            raise _Exception.AlreadyConnected(vehicle=self)

        if not self.connection_string:
            raise _Exception.ConnectionStringNotSpecified(vehicle=self)


class Copter(Vehicle):
    def __init__(self):
        super().__init__()


class Plane(Vehicle):
    def __init__(self):
        super().__init__()
