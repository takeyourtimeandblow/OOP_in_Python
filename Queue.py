class Queue:
    def __init__(self, *args):
        try:
            if len(args) == 0:
                raise TypeError(
                    f'{self.__class__.__name__} cant initialize without at least 1 argument ({len(args)} given)'
                )
            self.__lst = list(args)
        finally:
            pass

    def __str__(self):
        return f'[{' -> '.join(map(str, self.__lst))}]'

    def __repr__(self):
        return self.__lst

    def __add__(self, other):
        return Queue(*(self.__lst + other.__lst))

    def __iadd__(self, other):
        self.__lst += other.__lst
        return Queue(*self.__lst)

    def __eq__(self, other):
        return self.__lst == other.__lst

    def __rshift__(self, n):
        try:
            return Queue(*self.__lst[n:])
        except IndexError:
            return Queue(*[])

    def append(self, *args):
        try:
            if len(args) == 0:
                raise TypeError(f'Queue.append(self, *args) must take at least 1 argument ({len(args)} given)')
            self.__lst += args
        finally:
            pass

    def copy(self):
        return Queue(*self.__lst)

    def pop(self):
        return self.__lst.pop(0)

    def extend(self, other):
        self.__lst += other.__lst

    def __next__(self):
        return Queue(*self.__lst[1:])

    def next(self):
        return Queue(*self.__lst[1:])


q1 = Queue (1, 2, 3)
print(q1)
q1.append(4,5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue (1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)

