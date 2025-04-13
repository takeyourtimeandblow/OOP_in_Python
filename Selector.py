class Selector:
    nums: list[int]
    def __init__(self, a):
        self.nums = a
    def get_odds(self):
        return [i for i in self.nums if i % 2]
    def get_evens(self):
        return [i for i in self.nums if not i % 2]


print((sel := Selector(list(range(10)))).get_evens())
print(sel.get_odds())