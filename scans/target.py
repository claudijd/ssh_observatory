import socket
import sys


class Target:
    def __init__(self, target):
        self.target = target

    def valid_ip(self):
        try:
            ipaddress.ip_address(self.target)
            return True
        except:
            return False

    def valid_fqdn(self):
        try:
            socket.gethostbyname(self.target)
            return True
        except socket.error:
            return False

    def valid(self):
        # Needed for Python2 unicode nuances
        if sys.version_info[0] < 3:
            if type(input) in [str, unicode]:
                return False
        else:
            if not isinstance(self.target, str):
                return False

        starts_with_anti_patterns = [
            '127.0.0',
            '10.',
            '172.',
            '192.168',
            '169.254.169.254'
        ]

        for pattern in starts_with_anti_patterns:
            if self.target.startswith(pattern):
                return False

        if self.valid_ip() or self.valid_fqdn():
            return True

        return False
