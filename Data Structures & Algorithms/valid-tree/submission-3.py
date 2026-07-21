class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        seen = set()
        adjList = [[] for i in range(n)]
        
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        

        def dfs(node, parent):

            if node in seen:
                return False
            
            seen.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False
            return True
                

        return dfs(0,-1) and len(seen) == n
