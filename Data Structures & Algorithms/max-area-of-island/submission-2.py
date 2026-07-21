class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1,0], [0,-1], [0,1]]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            seen.add((r,c))
            area = 1

            while q:
                r,c = q.popleft()

                for dr, dc in directions:
                    if ((r+dr) in range(ROWS) and
                        (c+dc) in range(COLS) and
                        grid[r+dr][c+dc] == 1 and
                        (r+dr,c+dc) not in seen
                        ):
                    
                        area += 1
                        q.append((r+dr, c+dc))
                        seen.add((r+dr, c+dc))
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in seen:
                    max_area = max(max_area, bfs(r,c))
        
        return max_area
