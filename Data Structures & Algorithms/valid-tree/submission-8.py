class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()
        def dfs(node, prevNode):
            if node in visit:
                return False
                
            visit.add(node)

            for nei in adjList[node]:
                if nei == prevNode:
                    continue

                if not dfs(nei, node):
                    return False
            return True    

        return dfs(0, -1) and len(visit) == n
