class Solution:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        c = a // b
        if c < 0 and a % b != 0:
            return c + 1
        return c

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
        }
        stack = []
        for token in tokens:
            if token in operators:
                print(f'{stack}, {token}: ', end='')
                b = stack.pop()
                a = stack.pop()
                c = operators[token](a, b)
                stack.append(c)
                print(f'{a} {token} {b} = {c}')
            else:
                stack.append(int(token))
        if len(stack) != 1:
            raise ValueError('invalid input')
        return stack[0]