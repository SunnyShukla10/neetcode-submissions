
'''
cap = 2
cache = {}
left <->  <->  <-> right  

.put(1, 10)
cache = {1: LinkedNode(value, next, prev)}
left <-> 10 <-> right  

.put(2, 15)
cache = {1: LinkedNode(10, next, prev), 2: LinkedNode(15, next, prev)}
left <-> 10 <-> 15 <-> right

.get(0): returned -1
.get(2): returned 15
    left <-> 10 <-> 15 <-> right

.get(1): returned 10
    left <-> 15 <-> 10 <-> right


'''

class LinkedNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = LinkedNode(-1, 0), LinkedNode(-1, 0)
        self.left.next, self.right.prev = self.right, self.left

    
    def add(self, node):
        prev = self.right.prev
        prev.next, node.next = node, self.right
        node.prev, self.right.prev = prev, node
    
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        val_node = self.cache[key]

        self.remove(val_node)
        self.add(val_node)
        
        return val_node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = LinkedNode(key, value)
        
        self.add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.cap:
            to_remove = self.left.next
            self.remove(to_remove)
            del self.cache[to_remove.key]
        
        