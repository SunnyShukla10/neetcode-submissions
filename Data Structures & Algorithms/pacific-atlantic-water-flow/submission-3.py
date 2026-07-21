class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def dfs(r,c,prevHeight,visit):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or prevHeight > heights[r][c]:
                return
            
            visit.add((r,c))
            for dr,dc in dirs:
                nr,nc = dr+r, dc+c
                dfs(nr,nc,heights[r][c], visit)
        

        for i in range(ROWS):
            dfs(i, 0, heights[i][0],pac)
            dfs(i, COLS-1, heights[i][COLS-1],atl)

        for i in range(COLS):
            dfs(0,i, heights[0][i], pac)
            dfs(ROWS-1,i,heights[ROWS-1][i], atl)

        res = []
        for pair in pac:
            if pair in atl:
                res.append(list(pair))
        
        return res