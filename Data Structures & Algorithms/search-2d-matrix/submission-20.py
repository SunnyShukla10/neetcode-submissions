class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            m_row = (top + bottom) // 2

            if target > matrix[m_row][-1]:
                top = m_row + 1
            elif target < matrix[m_row][0]:
                bottom = m_row - 1
            else:
                break
        
        print("Middle row: ", m_row)
        if top > bottom:
            return False
        
        l,r = 0, COLS-1

        while l <= r:
            m = (r + l) // 2

            if target > matrix[m_row][m]:
                l = m + 1
            elif target < matrix[m_row][m]:
                r = m - 1
            else:
                return True
        
        return False
