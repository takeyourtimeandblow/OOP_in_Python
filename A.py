class A:
    def __str__(self):
        return f'A.__str__ method'
    def hello(self) -> None:
        print("Hello")
class B:
    def __str__(self):
        return f'B.__str__ method'
    def good_evening(self):
        print("Good Evening")
class C(A, B):
    pass
class D(B, A):
    pass


if __name__ == "__main__":
    print(c := C())
    print(d := D())
    print(isinstance(c, A), isinstance(d, B))
