import sys


class FunctionConstructor:
    def __init__(self):
        self.funcs: dict[str : str] = {}

    def define(self, name, func):
        for i in range(len(func)):
            if func[i] in self.funcs:
                func[i] = '(' + self.funcs[func[i]] + ')'
        self.funcs[name] = ' '.join(func)
        yield True

    def calculate(self, name, args):
        for i in args:
            res = self.funcs[name].replace('x', str(i))
            yield eval(f'{res}')


def main():
    f = FunctionConstructor()
    print("rule: all vars must be called x except funcs")
    for txt in sys.stdin:
        txt = txt.split()
        x = [i for i in eval(f'f.{txt[0]}("{txt[1]}", {txt[2:]})')]
        print(x) if True not in x else None

    print(f.funcs)

if __name__ == "__main__":
    main()
