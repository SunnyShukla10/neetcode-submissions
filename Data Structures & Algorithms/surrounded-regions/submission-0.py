class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        # no need for visited since each element will be turned into a diff symbol if visited

        def dfs(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                board[r][c] != "O"):
                return 
            board[r][c] = "*"
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)

        
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1,c)
        
        # Iterate over the grid again and mark "*" as 0's and 0's as 1

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "*":
                    board[r][c] = "O"
                
         
