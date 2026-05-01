class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_n = sum(nums)
        curr = 0

        for i in range(n):
            curr += i*nums[i]

        max_res = curr
        
        for i in range(1,n):
            curr = curr + sum_n - n*nums[n-i]
            max_res = max(max_res, curr)
        
        return max_res
            
