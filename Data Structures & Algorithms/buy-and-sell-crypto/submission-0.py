class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                if j > i:
                    profit = prices[j] - prices[i]
                    best = max(best, profit)

        return best


        