class Triangle:
    t: tuple[int]
    def __init__(self, *args: int):
        try:
            if len(args) != 3:
                raise TypeError(f"Triangle must take 3 arguments ({len(args)} given)")
            self.t = args
        finally:
            pass
    def perimeter(self) -> int:
        return sum(self.t)


class EquilateralTriangle(Triangle):
    def __init__(self, edge):
        super().__init__(edge, edge, edge)

tr = Triangle(1, 2, 3)

tr1 = EquilateralTriangle(3)

print(tr.perimeter())

print(tr1.t)