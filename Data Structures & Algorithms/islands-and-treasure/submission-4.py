class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi source BFS
        ROWS, COLS, INF = len(grid), len(grid[0]), 2147483647
        dirs =[[-1,0], [1,0], [0,1], [0,-1]]
        q = deque()
        seen = set()
        dist = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    seen.add((i,j))
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                    if nr in range(0, ROWS) and nc in range(0, COLS) and grid[nr][nc] == INF and (nr,nc) not in seen:
                        q.append((nr,nc))
                        seen.add((nr,nc))
            dist += 1        
