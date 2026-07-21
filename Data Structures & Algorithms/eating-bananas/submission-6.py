class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res =r 

        while l <= r:
            m = (l+r) // 2

            num_hours = 0
            for p in piles:
                num_hours += math.ceil(float(p) / m)
            

            if num_hours > h:
                l = m + 1
            else:
                res = m
                r = m - 1

        return res