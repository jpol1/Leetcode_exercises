class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for idx in range(len(prices) - 1):
            if prices[idx] < prices[idx+1]:
                res += prices[idx+1] - prices[idx]
        return res