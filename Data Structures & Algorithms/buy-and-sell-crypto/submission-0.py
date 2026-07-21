class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # want left to be at a small
        # want right to be at a bigger num

        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:  
                l = r
            r += 1
        return profit