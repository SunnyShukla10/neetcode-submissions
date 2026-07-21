class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1,0],[-1,0],[0,-1],[0,1]]
        max_area = 0
        visit = set()

        def dfs(row, col):

            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0 or (row, col) in visit:
                return 0
            area = 1
            visit.add((row,col))

            for dr, dc in dirs:
                area += dfs(row+dr, col + dc)
            
            return area
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_area = max(max_area,dfs(i,j))
        
        return max_area
