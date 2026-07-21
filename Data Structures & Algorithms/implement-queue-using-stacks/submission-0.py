class MyQueue:

    '''
    stack1 = []
    stack2 = []

    add 1
    stack1 = [1]
    stack2 = []

    peek
    stack1 = [1] ==> return 1

    add 2
    stack1 = [2,1]
    stack2 = []

    remove 
        step 1
            stack1 = []
            stack2 = [1, 2]
        res = 1

        stack2 = []
        stack1 = [2]
        return 1
    
    stack1 = [2]
    stack2 = []

    add 3, 1, 4
    stack1 = [4,1,3,2]
    stack2 = []

    peek
        step 1
            stack1 = []
            stack2 = [2,3,1,4]
            res = 2
            stack1


    '''


    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return res

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2[-1]

        while self.stack2:
            self.stack1.append(self.stack2.pop())
       
        return res
    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()