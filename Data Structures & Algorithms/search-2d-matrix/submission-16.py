class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # look at the last value for the rows that arent the last row
        # look at the first value of the last row and then go from there
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (r+l)//2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
        
        if not(l <= r):
            return False
        row = (r+l)//2
        l, r = 0, len(matrix[row]) -1
        while l <= r:
            m = (r+l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
