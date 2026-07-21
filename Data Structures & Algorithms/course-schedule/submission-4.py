class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for course, prerq in prerequisites:
            preMap[course].append(prerq)
        
        seen = set()
        def dfs(c):
            if c in seen:
                # revisiting 
                return False
            
            if preMap[c] == []:
                return True
            
            # Take course and add into visit and go to neighbors
            seen.add(c)

            for pre in preMap[c]:
                if not dfs(pre): 
                    return False
                
            seen.remove(c)
            preMap[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c): 
                return False
        
        return True
        
