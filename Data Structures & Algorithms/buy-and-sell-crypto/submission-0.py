class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit =0
        maxprice=0
        for i in range (len(prices)-1,-1,-1):
            print(i, prices[i])
            if prices[i]>maxprice:
                maxprice =prices[i]
            if maxprice -prices[i] > maxprofit:
                maxprofit = maxprice -prices[i]
        return maxprofit
        