class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grid = collections.defaultdict(set) # key = (row / 3, col / 3), value is the hashset of that 3x3 grid

        for r in range(len(board)):
            for c in range(len(board[r])): 
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[(r//3,c//3)]):
                    return False # there was a duplicate in row, col, or the grid
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r//3,c//3)].add(board[r][c])
        return True

        