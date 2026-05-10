class MinStack:

    def __init__(self):
        self.stack = []
        self.minsofar = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minsofar) > 0:
            self.minsofar.append(min(val, self.minsofar[-1]))
        else:
            self.minsofar.append(val)

    def pop(self) -> None:
        self.minsofar.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minsofar[-1]
