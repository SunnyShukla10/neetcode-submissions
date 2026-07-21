class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # look at the last value for the rows that arent the last row
        # look at the first value of the last row and then go from there

        l, r = 0, len(matrix)-1
        # find the row where the value falls
        while l <= r:
            row = (l + r) // 2 
            if target > matrix[row][-1]:
                l = row + 1                
            elif target < matrix[row][0]:
                r = row - 1  
            else:
                break
        if not (l <= r):
            return False

        row = (l+r) // 2
        # preform binary search on the row
        l , r = 0, len(matrix[row]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True
        
        return False