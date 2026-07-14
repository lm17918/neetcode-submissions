class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot=0
        sellprice=None
        buyprice=None
        for i in range(len(prices)-1,-1,-1):
            print("prices[i]",prices[i],"sellprice",sellprice,"buyprice",buyprice)
            if buyprice is None and (sellprice is None or sellprice<prices[i]):
                print("if sellprice is None or sellprice<prices[i]:")
                sellprice=prices[i]
            elif buyprice is None or prices[i] <buyprice:
                print("elif buyprice is None or prices[i] <buyprice:")
                buyprice=prices[i]
            else:
                print("tot ")
                tot += sellprice-buyprice
                sellprice=prices[i]
                buyprice=None
        if buyprice is not None:
            tot += sellprice-buyprice
        return tot