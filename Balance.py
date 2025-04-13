class Balance:
    l: int
    r: int
    def __init__(self, l=0, r=0):
        self.l = l
        self.r = r
    def add_left(self, i):
        self.l += i
    def add_right(self, i):
        self.r += i
    def result(self):
        return [
            j for i, j in {
                self.l > self.r : "L",
                self.r > self.l : "R",
            }.items() if i
        ] or "="

bal = Balance()

bal.add_left(10)
bal.add_left(20)
print(bal.result())
bal.add_right(30)
print(bal.result())