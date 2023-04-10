class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if n > self._capacity :
            raise ValueError("exceeded capacity")
        if self._size + n > self._capacity:
            raise ValueError("not enough space")
        self._size += n

    def withdraw(self, n):
        if n > self._size :
            raise ValueError("less qty")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(11)
print(jar)
jar.withdraw(1)
print(jar)
