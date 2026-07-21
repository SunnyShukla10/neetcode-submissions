class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.left_dummy, self.right_dummy = Node(0,0), Node(0,0)
        self.left_dummy.next, self.right_dummy.prev = self.right_dummy, self.left_dummy        

    def remove(self,node):
        right, left = node.next, node.prev
        left.next, right.prev = right, left

    def add(self,node):
        prev_node = self.right_dummy.prev
        prev_node.next, node.next = node, self.right_dummy
        node.prev, self.right_dummy.prev = prev_node, node

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]

            self.remove(node)
            self.add(node)

            return node.val
        return -1 
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
                
        
        to_add = Node(key, value)
        self.d[key] = to_add
        self.add(to_add)

        if len(self.d) > self.cap:
            # so you delete the right node from the dictironary
            lru = self.left_dummy.next
            self.remove(lru)
            del self.d[lru.key]
        
        
