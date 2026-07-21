class MyStack:

    '''
    STACK
    add: 2 3 4
    stack: [2,3,4] <- front
    pop
    stack: [2,3]
    
    QUEUE
    add: 2 3 4
    q = front -> [2,3,4]
    q2 = [   ]
    pop
    q= [3,4]

    '''
    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        num_rot = len(self.q1)

        self.q1.append(x)

        # was empty beofre adding
        if num_rot == 0:
            return 
        else:
            # Rotate elements
            for i in range(num_rot):
                val = self.q1.popleft()
                self.q1.append(val)


    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()