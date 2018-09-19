import socket


class Port:
    def __init__(self, port):
        self.port = port

    def valid(self):
        if not isinstance(self.port, int):
            return False

        if self.port == 22:
            return True

        return False
