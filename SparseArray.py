class SparseArray:
    def __init__(self):
        self.dct = dict()
    def __getitem__(self, item):
        try:
            return self.dct[item]
        except KeyError:
            return 0 or None
    def __setitem__(self, key, value):
        self.dct[key] = value



sl = SparseArray()

sl[1] = 12

print(sl[0])
print(sl[1])

index = 1_000_000

sl[index] = 20

for i in range (0, index+1, 1000):
    print(sl[i])

