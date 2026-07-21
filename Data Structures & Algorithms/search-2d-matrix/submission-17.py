class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top, bot = 0, ROWS - 1

        valRow = 0
        while top <= bot:
            m = (top + bot) // 2

            if matrix[m][0] > target:
                bot = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                print(f"found row at idx {m} of matrix")
                valRow = m
                break
        
        l,r = 0, COLS -1 
        
        while l <= r:
            m = ((r-l) // 2) + l

            if matrix[valRow][m] > target:
                r = m - 1
            elif matrix[valRow][m] < target:
                l = m + 1
            else:
                return True
        
        return False