class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_val = r

        while l<=r:
            k = l + ((r-l)//2)
            num_hours = 0
            for n in piles:
                num_hours += math.ceil(float(n)/k)
            
            if num_hours <= h:
                min_val = min(min_val, k)
                r = k - 1
            else:
                l = k + 1
        return min_val