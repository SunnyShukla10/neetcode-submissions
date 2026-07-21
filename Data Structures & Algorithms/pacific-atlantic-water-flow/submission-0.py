class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                (r,c) in visit or heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))

            # each direction
            for dr, dc in dirs:
                nr,nc = r + dr, c+dc
                dfs(nr,nc,visit,heights[r][c])
                

        for c in range(COLS):
            dfs(0,c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS -1, atl, heights[r][COLS-1])
        
        res = []
        for p in pac:
            for a in atl:
                if p == a:
                    res.append(a)
        
        return res