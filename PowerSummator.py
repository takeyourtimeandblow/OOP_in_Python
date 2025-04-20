from typing import override
from Summator import Summator

class PowerSummator(Summator):
    def __init__(self, pow: int):
        super().__init__(pow)

    @override
    def transform(self, n):
        return n ** self.pow

if __name__ == "__main__":
    print((s := PowerSummator(3)).sum(5))
