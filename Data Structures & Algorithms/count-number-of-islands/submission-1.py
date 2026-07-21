class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.res = 0
        seen = set()

        def dfs(r, c):
            if r >= ROWS or r < 0 or c < 0 or c >= COLS or grid[r][c] == "0" or (r,c) in seen:
                return 
            
            seen.add((r,c))

            # all directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                print(grid[r][c])
                if grid[r][c] == "1" and not (r,c) in seen:
                    print(r, " ", c)
                    dfs(r, c)    
                    self.res += 1
                    print(seen)
                    
        
        return self.res