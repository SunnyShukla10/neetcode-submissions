class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:    
        l, r = 0, len(matrix) - 1
        row = 0
        while l <= r:
            row = (l + r) // 2
            if target < matrix[row][0]:
                r = row - 1
            elif target > matrix[row][-1]:
                l = row + 1
            else:
                break
        
        if l > r:
            return False
        
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2

            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        
        return False