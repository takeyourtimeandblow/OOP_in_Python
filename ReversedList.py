from typing import override


class ReversedList:
    lst: list[int]
    def __init__(self, a):
        self.lst = list(reversed(a))
    def __call__(self):
        return self.lst
    def __str__(self):
        return str(self.lst)
    def __getitem__(self, item):
        return self.lst[item]
    def __len__(self):
        return len(self.lst)


print(rl := ReversedList(list(range(100))))

for i in range(len(rl)):
    print(rl[i])

