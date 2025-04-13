class BigBell:
    even: bool
    def __init__(self):
        self.even = False
    def sound(self):
        if self.even:
            print("dong")
        else:
            print("ding")
        self.even = not self.even

bell = BigBell()
for i in range(10):
    bell.sound()