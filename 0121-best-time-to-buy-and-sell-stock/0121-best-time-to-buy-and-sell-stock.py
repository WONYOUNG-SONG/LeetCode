class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_val = 0
        
        for price in prices[1:]:
            max_val = max(max_val, price - min_val)
            min_val = min(min_val, price)
    
        return max_val
