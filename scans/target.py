import socket


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
