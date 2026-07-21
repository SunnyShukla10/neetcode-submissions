class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        dirs = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col, visited, prevHeight):
            
            # invalid
            if row >= ROWS or row < 0 or col < 0 or col >= COLS or (row, col) in visited or heights[row][col] < prevHeight:
                return

            visited.add((row,col))
            
            for dr,dc in dirs:
                nr, nc = row + dr, col + dc
                dfs(nr, nc, visited, heights[row][col]) 


        for i in range(COLS):
            dfs(0, i, pac, heights[0][i])
            dfs(ROWS-1, i, atl, heights[ROWS-1][i])

        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS-1, atl, heights[i][COLS-1])
    
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res
