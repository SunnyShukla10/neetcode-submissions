class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colsDict = defaultdict(set)
        rowsDict = defaultdict(set)
        squareDict = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in colsDict[c] or board[r][c] in rowsDict[r] or board[r][c] in squareDict[(r//3, c//3)]:
                    return False

                colsDict[c].add(board[r][c]) 
                rowsDict[r].add(board[r][c])
                squareDict[(r//3, c//3)].add(board[r][c])

        
        return True