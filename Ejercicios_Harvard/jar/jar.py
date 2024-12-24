class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        a = self.size + n
        if a > self._capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    galleta = Jar(100)
    galleta.deposit(11)
    galleta.withdraw(5)
    print(galleta)


if __name__ == "__main__":
    main()
