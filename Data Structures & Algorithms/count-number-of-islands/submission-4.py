class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        islands = 0

        def bfs(r,c):
            
            q = deque()
            q.append((r,c))
            grid[r][c] = "2"

            while q:
                r, c = q.popleft() 
                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                    if nr in range(0,ROWS) and nc in range(0,COLS) and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        grid[nr][nc] = "2"



        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    print(grid)
                    bfs(i,j)
                    islands += 1

        return islands