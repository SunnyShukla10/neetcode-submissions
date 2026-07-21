class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
       self.cache = {}
       self.capacity = capacity
       self.right, self.left = Node(0,0), Node(0,0)
       self.left.next, self.right.prev = self.right, self.left

    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        mru_prev = self.right.prev
        mru_prev.next = self.right.prev = node
        node.next, node.prev = self.right, mru_prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # update LRU, MRU
        self.remove(self.cache[key])
        self.insert(self.cache[key])    
        
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

