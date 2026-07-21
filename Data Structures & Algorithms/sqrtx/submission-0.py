class Solution:
    def mySqrt(self, x: int) -> int:
        

        '''
        1 2 3 4 5 6 7 8 9
        m = 5, val = m * m
        m = 2. val = 2 * 2

        1 2 3 4 5 6 7 8 9 10 11 12 13
        m = 7, val = 49
        m = 3, val = 9
        m = 5, val = 25
        m = 4, val = 16
        r = 3, l = 4
        
        1 2 3 4
        m = 2, val = 4

        1 2 3
        m = 2, val = 4
        m = 1, val = 1


        1 2 3 4 5
        m = 3, val = 9
        m = 1, val = 1
        m = 2, val = 4
        '''

        if x == 0:
            return 0
        
        l,r = 1, x

        while l <= r:
            m = (r + l) // 2
            sq = m * m
            if sq < x:
                l = m + 1
            elif sq > x:
                r = m - 1
            else:
                return m
                
        return r





        
