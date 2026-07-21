"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {} # seen set and the copy 

        def dfs(node):
            if node in hashmap:
                print(node.val, "is already in")
                return hashmap[node]
            
            copy = Node(node.val)
            print("created new copy for ", node.val)
            hashmap[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        if node:
            dfs(node)
            return hashmap[node]
        else:
            return None
        