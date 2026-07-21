class LinkedNode:
    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.left = LinkedNode(0, None, None)
        self.right = LinkedNode(0, None, self.left)
        self.left.next = self.right
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        prev = self.right.prev
        newnode = LinkedNode(value, self.right, prev)
        prev.next = newnode
        self.right.prev = newnode
        self.cap -= 1
        
        self.printCQ()
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 

        newnext = self.left.next.next
        self.left.next = newnext
        newnext.prev = self.left

        self.cap += 1
        self.printCQ()
        return True

    def Front(self) -> int:
        return self.left.next.val if not self.isEmpty() else -1 
    
    def Rear(self) -> int:
        return self.right.prev.val if not self.isEmpty() else -1
    
    def isEmpty(self) -> bool:
        return self.left.next == self.right
    
    def isFull(self) -> bool:
        return self.cap == 0

    def printCQ(self):
        cur = self.left.next
        print("start")
        while cur != self.right:
            print(f"{cur.val} ")
            cur = cur.next
        print("end")

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()