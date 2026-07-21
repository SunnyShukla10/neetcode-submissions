class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True


        adjMap = [[] for i in range(n)] 
        for s, e in edges:
            adjMap[s].append(e)
            adjMap[e].append(s)

        
        seen = set()

        def dfs(node, parent):
            if node in seen:
                return False

            neighbors = adjMap[node]
            seen.add(node)
            for nei in neighbors:
                if nei == parent:
                    continue
                
                if nei in seen:
                    return False
                
                if not dfs(nei, node):
                    return False
                
            return True
        
        return dfs(0,-1) and len(seen) == n
                    




