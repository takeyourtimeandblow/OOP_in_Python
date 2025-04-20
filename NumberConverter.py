class NumberConverter:
    def __init__(self, nums):
        self.lst = nums

    def make_negative(self):
        self.lst = [-i for i in self.lst]

    def square(self):
        self.lst = [i**2 for i in self.lst]
    def strange_command(self):
        for i in range(len(self.lst)):
            if self.lst[i] % 5 == 0:
                self.lst[i]+=1

def main():
    nums = NumberConverter(list(map(int, input().split())))
    no_of_commands = int(input())
    for _ in range(no_of_commands):
        match input():
            case "make_negative":
                nums.make_negative()
            case "square":
                nums.square()
            case "strange_command":
                nums.strange_command()
    print(nums.lst)

if __name__ == "__main__":
    main()