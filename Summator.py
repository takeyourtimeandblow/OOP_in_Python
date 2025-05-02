from typing import override
from typing import Final

class Summator: # base
    pow: int
    def __init__(self, n=1):
        self.pow = n

    def transform(self, n):
        return n
    def sum(self, n):
        return sum([i ** self.pow for i in range(1, n + 1)])

class SquareSummator(Summator):
    def __init__(self):
        super().__init__(2)

    @override
    def transform(self, n):
        return n**self.pow

class CubeSummator(Summator):
    def __init__(self):
        super().__init__(3)

    @override
    def transform(self, n):
        n**self.pow

if __name__ == "__main__":
    N: Final[int] = 5

    print(f"Solved 1: {(s := Summator()).sum(N)} :: {int(N * (N + 1) / 2)}")
    print(f"Solved 1: {(s1 := SquareSummator()).sum(N)} :: {int(N * (N + 1) * (2 * N + 1) / 6)}")
    print(f"Solved 1: {(s2 := CubeSummator()).sum(N)} :: {int(N * (N + 1) / 2)**2}")
