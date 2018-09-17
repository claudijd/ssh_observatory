class Target:
    def __init__(self, target):
        self.target = target

    def valid(self):
        if self.target.startswith('127.0.0'):
            return False

        if self.target.startswith('10.') or self.target.startswith('172.') or self.target.startswith('192.168'):
            return False

        if self.target == "169.254.169.254":
            return False

        return True
