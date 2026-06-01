class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        cost.sort(reverse=True)
        for idx in range(len(cost)):
            if (idx+1) % 3 != 0:
                res += cost[idx]
        return res 