class FunctionCalculator:
    def __init__(self):
        self.functions = {}
        self.functions['x'] = lambda x: x
        self.functions['sqrt_fun'] = lambda x: x ** 0.5

    def calculate_function(self, func_name, x):
        if func_name in self.functions:
            return self.functions[func_name](x)
        else:
            raise ValueError(f"Function {func_name} is not defined.")

    def define_function(self, definition):
        parts = definition.split()
        if len(parts) != 5:
            raise ValueError("Invalid function definition.")

        _, func_name, arg1, operation, arg2 = parts

        def func(x):
            val1 = float(arg1) if arg1.isdigit() or arg1[0] == '-' else self.calculate_function(arg1, x)
            val2 = float(arg2) if arg2.isdigit() or arg2[0] == '-' else self.calculate_function(arg2, x)

            if operation == '+':
                return val1 + val2
            elif operation == '-':
                return val1 - val2
            elif operation == '*':
                return val1 * val2
            elif operation == '/':
                return val1 / val2
            else:
                raise ValueError(f"Unknown operation {operation}.")

        self.functions[func_name] = func

    def calculate(self, command):
        parts = command.split()
        func_name = parts[1]
        results = [self.calculate_function(func_name, float(x)) for x in parts[2:]]
        return results


def main():
    calculator = FunctionCalculator()

    while True:
        try:
            line = input().strip()
            if line.startswith("define"):
                calculator.define_function(line)
            elif line.startswith("calculate"):
                results = calculator.calculate(line)
                print(" ".join(map(str, results)))
            else:
                print(f"Unknown command: {line}")
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
