class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_map = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == ".":
                    continue

                r_idx, c_idx = r//3, c//3
                
                if val in rows[r] or val in cols[c] or val in board_map[(r_idx, c_idx)]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                board_map[(r_idx, c_idx)].add(val)

        return True