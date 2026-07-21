class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # since we are dealing with duplicates can use a set
        # need to store set in some data strucutre because there are different cols, rows, and combo of rows and cols

        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):

                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])

        return True