class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        left = 0

        for right in range(1, len(prices)):  
            if prices[right] < prices[left]:
                left = right         
            else:
                best = max(best, prices[right] - prices[left])




        """
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                if j > i:
                    profit = prices[j] - prices[i]
                    best = max(best, profit)
        """

        return best


        