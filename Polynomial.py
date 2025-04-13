class Polynomial:
    def __init__(self, c: list):
        self.c = c
    def __call__(self, x):
        if x == 0:
            return self.c[0]
        result = 0
        for i in range(len(self.c)):
            result += self.c[i] * x**i
        return result
    def __add__(self, other):
        temp = self.c
        temp1 = other.c

        temp.extend([0, ] * (len(temp1) - len(temp)))
        temp1.extend([0, ] * (len(temp) - len(temp1)))

        result = map(sum, zip(temp,temp1))

        return Polynomial(list(result))


poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))




