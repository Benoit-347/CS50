# the class structure here has no user defined 'setter' hence, when assigning capacity, it will not be redirected to any setter;
    # further more direct assignment may not happen as the getter will keep getting called, hence we need to use '_' on house during assignment to bypass getter.
class Jar:
    def __init__(self, capacity=12):
        if capacity <0:
            raise ValueError
        self._capacity = capacity
        self.n = 0

    def __str__(self):
        return "🍪"*self.n

    def deposit(self, n):
        if n + self.n > self.capacity:
            raise ValueError
        self.n += n

    def withdraw(self, n):
        if n > self.n:
            raise ValueError
        self.n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.n
