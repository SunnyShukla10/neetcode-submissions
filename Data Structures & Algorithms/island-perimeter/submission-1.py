class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        self.res = 0
        seen = set()

        def dfs(r, c):

            if (r,c) in seen:
                return
            
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == 0:
                self.res += 1
                return
            
            seen.add((r, c))

            # every direction
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)

            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    print(r, " ", c)
                    dfs(r,c)
                    return self.res
        

        return 0
        

