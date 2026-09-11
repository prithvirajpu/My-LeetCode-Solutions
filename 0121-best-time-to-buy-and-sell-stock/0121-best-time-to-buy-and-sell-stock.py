class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minValue=prices[0]
        maxProfit=0

        for i in prices:
            if i< minValue:
                minValue=i
            maxProfit=max(maxProfit,i-minValue)  
        return maxProfit































