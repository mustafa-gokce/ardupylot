class ArdupylotBaseException(Exception):
    """Ardupylot base exception"""

    def __init__(self, vehicle, message=None):
        if message is None:
            message = f"Base exception for vehicle {vehicle}"
        super(Exception, self).__init__(message)
        self.vehicle = vehicle


class ConnectionStringNotSpecified(ArdupylotBaseException):
    """Connection string not specified exception"""

    def __init__(self, vehicle):
        super().__init__(message=f"Connection string not specified for vehicle {vehicle}", vehicle=vehicle)


class AlreadyConnected(ArdupylotBaseException):
    """Already connected exception"""

    def __init__(self, vehicle):
        super().__init__(message=f"Already connected to vehicle {vehicle}", vehicle=vehicle)
