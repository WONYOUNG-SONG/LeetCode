class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            current_profit = price - min_price
            if price < min_price:
                min_price = price
            elif current_profit > max_profit:
                max_profit = current_profit
    
        return max_profit
