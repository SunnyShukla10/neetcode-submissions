class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS, INF = len(grid), len(grid[0]), 2147483647
        q = deque()
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))


        def traverseLand(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                grid[r][c] == -1 or (r,c) in seen):
                return
            
            q.append((r,c))
            seen.add((r,c))


        distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                # each direction
                traverseLand(r + 1, c)
                traverseLand(r - 1, c)
                traverseLand(r, c + 1)
                traverseLand(r, c - 1)
            distance += 1
        
    

