class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, res
        # 1 2 3 4 5 6 7 8 9 10 11
        #           ^

        while l <= r:
            m = (l+r) // 2

            num_hours = 0
            for p in piles:
                num_hours += math.ceil(p / m)
            
            print(f"for k of {m} it took {num_hours} hours")

            if num_hours > h:
                # go to the next hour
                l = m + 1
            else:
                r = m - 1
                res = min(res, m)
                

        return res