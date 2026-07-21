class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [LinkedNode(None, None) for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        idx = (key % len(self.hashmap))
        node = self.hashmap[idx]
        # Iterate over the chain 
        while node.next:
            if node.next.key == key:
                # Add the new linked node 
                node.next = LinkedNode(key, value)
                return 
            node = node.next
        node.next = LinkedNode(key, value)
        
    def get(self, key: int) -> int:
        idx = (key % len(self.hashmap))
        node = self.hashmap[idx]

        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next

        return -1 # not found

    def remove(self, key: int) -> None:
        idx = (key % len(self.hashmap))
        node = self.hashmap[idx]

        if self.hashmap[idx] == None:
            return 
        
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return 
            node = node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)