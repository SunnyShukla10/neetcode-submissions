class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # look at the last value for the rows that arent the last row
        # look at the first value of the last row and then go from there

        l, r = 0, len(matrix)-1
        val_row = -1
        # find the row where the value falls
        while l <= r:
            if target <= matrix[l][-1]:
                val_row = l
                break
            elif target >= matrix[r][0]:
                val_row = r
                break
            else:
                l+=1
                r-=1
        print(f'row is {val_row}')

        # preform binary search on the val_row
        l , r = 0, len(matrix[val_row]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > matrix[val_row][m]:
                l = m + 1
            elif target < matrix[val_row][m]:
                r = m - 1
            else: 
                return True
        
        return False