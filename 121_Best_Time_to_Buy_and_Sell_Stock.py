class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        date = len(prices)
        buy_price = prices[0]
        max_profit = 0

        for i in range(1, date):
            if prices[i] - buy_price > max_profit:
                max_profit = prices[i] - buy_price
            elif prices[i] < buy_price:
                buy_price = prices[i]
        return max_profit