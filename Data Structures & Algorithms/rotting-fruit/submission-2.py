class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
        
        
        def rotFruit(r,c):
            if ( r >= ROWS or r < 0 or c < 0 or c >= COLS or 
                grid[r][c] == 0 or (r,c) in seen):
                return
            
            q.append((r,c))
            seen.add((r,c))

        time = 0
        while q:
            # iterate over each level
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2

                rotFruit(r+1,c)
                rotFruit(r-1,c)
                rotFruit(r,c+1)
                rotFruit(r,c-1)
            
            time += 1 if q else 0
        print(grid)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return time