class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        seen = set()
        max_area = 0


        def dfs(r,c):
        
            if r >= ROWS or r < 0 or c < 0 or c >= COLS or grid[r][c] == 0 or (r,c) in seen:
                return 0

            seen.add((r,c))
            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) 
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in seen:
                    area = dfs(r,c)
                    max_area = max(max_area, area)


        return max_area