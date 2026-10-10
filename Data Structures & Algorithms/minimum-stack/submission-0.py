class MinStack:

    def __init__(self):
        stack = []
        self.stack = stack
        

    def push(self, val: int) -> None:
        self.stack.reverse()
        self.stack.append(val)
        self.stack.reverse()



    def pop(self) -> None:
        self.stack.remove(self.stack[0])

        
    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return min(self.stack)
        
