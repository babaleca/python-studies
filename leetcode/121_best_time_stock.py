class Solution(object):
    def maxProfit(self, prices):
        min=10000
        max=0
        lucro=0
        for i in range(len(prices)):
            if prices[i]<min: 
                min = prices[i]
            sub = prices[i]-min
            if(sub>lucro): lucro = sub
             
        return lucro