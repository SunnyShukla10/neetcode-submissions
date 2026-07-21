class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}

        for u, v in prerequisites:
            adjList[u].append(v)

        seen = set()
        
        def dfs(c) -> bool:
            
            if c in seen:
                return False
        
            if not adjList[c]:
                return True 
                
            seen.add(c)

            for nei in adjList[c]:
                if not dfs(nei):
                    return False
            seen.remove(c)
            adjList[c] = []
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

        