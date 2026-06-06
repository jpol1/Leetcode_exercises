class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        right_sum = sum(nums)
        left_sum = 0
        for idx in range(len(nums)):
            tmp = nums[idx]
            right_sum -= tmp
            res.append(abs(right_sum-left_sum))
            left_sum += tmp
        return res