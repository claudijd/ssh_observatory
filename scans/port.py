import socket


class Port:
    def __init__(self, port):
        self.port = port

    def valid(self):
        if not isinstance(self.port, int):
            return False

        return self.port == 22
