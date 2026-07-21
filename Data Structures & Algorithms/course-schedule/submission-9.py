class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for u, v  in prerequisites:
            adjList[u].append(v) # in order to finish a course dfs all of the prereqs (Which is why we have u -> v)
        
        visit = set()

        def dfs(node):
            print(node)
            print(visit)
            if node in visit:
                return False
            
            # course node can be completed
            if adjList[node] == []:
                return True

            visit.add(node)

            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            return True
        print(adjList)
        for crs in range(numCourses):
            if not dfs(crs):
                print("False ", crs)
                return False
        
        return True