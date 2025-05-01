import sys


class FunctionConstructor:
    def __init__(self):
        self.funcs: dict[str : str] = {} # name of function is key, function will be formated to string

    def define(self, name, func):
        for i in range(len(func)):
            if func[i] in self.funcs:
                func[i] = '(' + self.funcs[func[i]] + ')' # brackets to save priority of actions
        self.funcs[name] = ' '.join(func) # important to save space between all elements of function
        yield True # necessary, but 26's line will not work

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
        """if txt would be equal 'define f1 x * x'
        then upper argument to function eval should be equal:
        f.define("f1", ['x', '*', 'x'])
        """
        print(x) if True not in x else None # just ignore define call

    print(f.funcs)

if __name__ == "__main__":
    main()
