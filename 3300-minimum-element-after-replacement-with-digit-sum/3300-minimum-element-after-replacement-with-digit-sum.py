class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            res.append( sum([int(i) for i in str(num)]) )
        return min(res)