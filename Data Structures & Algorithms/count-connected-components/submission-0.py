class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for i in range(n)]
        res = 0

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for nei in adjList[node]:
                dfs(nei)

        for i in range(n):
            if i not in visit:
               dfs(i)
               res += 1
        return res