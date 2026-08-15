class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k
        
        while l <= r:
            m = (r + l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / m) 

            if hours <= h:
                k = m
                r = m - 1  
            else:
                l = m + 1
        
        return k