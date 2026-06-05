class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=False
        profit=0
        i=0
        while(i<len(prices)-2):
                if prices[i]<prices[i+1]:
                    if prices[i+1]>prices[i+2]:
                        profit+=prices[i+1]-prices[i]
                        i=i+2
                    else:
                        start = prices[i]
                        while(prices[i]<prices[i+1]):
                            i+=1
                            if i == len(prices)-1:
                                break
                        profit += prices[i]-start
                else:
                    i+=1
        if i<len(prices)-1 and prices[i]<prices[i+1]:
            profit+=prices[i+1]-prices[i]
        return profit