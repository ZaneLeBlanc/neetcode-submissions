class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = 101
        maxProfit = 0

        ptr = 0

        while ptr < len(prices):
            if prices[ptr] - smallest > maxProfit:
                maxProfit = prices[ptr] - smallest
            
            if prices[ptr] < smallest:
                smallest = prices[ptr]
            
            ptr+=1
        
        return maxProfit