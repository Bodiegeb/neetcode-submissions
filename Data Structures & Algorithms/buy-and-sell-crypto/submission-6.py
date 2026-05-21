class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        r = 1
        while r < len(prices):
            if(prices[r] > prices[l]):
                profit = prices[r] - prices[l]
                if profit > prof:
                    prof = profit
            else:
                l = r
            r+=1
        return prof