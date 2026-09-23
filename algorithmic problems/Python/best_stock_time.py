class Solution(object):
    def maxProfit(self, prices):
        min_price = float('-inf')
        maxProfit = float('inf')

        for price in prices:
            min_price = min(price, min_price)
            curr_profit = price - min_price
            maxProfit = max(curr_profit, maxProfit)

        return maxProfit