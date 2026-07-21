class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))

        while q:
            rotted = False
            print(q)
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in dirs:
                    nr, nc = r+dr, c+dc

                    if nr in range(0,ROWS) and nc in range(0,COLS) and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        rotted = True
            print(grid)
            if rotted:
                time += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return time