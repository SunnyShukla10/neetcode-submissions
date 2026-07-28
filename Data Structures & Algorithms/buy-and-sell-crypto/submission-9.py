class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_val = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                max_val = max(max_val, prices[r] - prices[l]) 
                continue
            l = r

        return max_val