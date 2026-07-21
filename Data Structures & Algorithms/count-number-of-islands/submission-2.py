class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        islands = 0
        directions = [[-1,0], [1,0], [0, -1], [0, 1]]

        def bfs(r,c):
            q = deque()
            q.append((r,c))

            while q:
                r,c = q.popleft()

                for dr, dc in directions:
                    if ((r + dr) in range(ROWS) and 
                        (c + dc) in range(COLS) and 
                        grid[r+dr][c+dc]=="1" and 
                        (r + dr, c + dc) not in seen):

                        q.append((r+dr, c+dc))
                        seen.add((r+dr, c+dc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1

        return islands