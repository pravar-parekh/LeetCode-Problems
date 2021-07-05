'''
Summary:-
    Simple stack operations. For each element in stack keep a value which maintains min value
    for it. Update this value when changes to stack are made.
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf")
        
    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val 
        self.stack.append([val,self.min])     

    def pop(self) -> None:
        to_return = self.stack.pop()
        if self.stack != []:
            self.min = self.stack[-1][1]
        else: 
            self.min = float("inf")

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()