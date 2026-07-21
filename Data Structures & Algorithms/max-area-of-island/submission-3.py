class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1,0],[-1,0],[0,-1],[0,1]]
        max_area = 0

        def dfs(row,col):
            
            # check bad cases
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0 or grid[row][col] == 2:
                return 0
            area = 1
            grid[row][col] = 2 # visited

            for dr, dc in dirs:
                area += dfs(dr+row,dc+col)
            
            return area
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
                

        return max_area        
