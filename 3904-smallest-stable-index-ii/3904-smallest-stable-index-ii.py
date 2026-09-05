class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        suffixmin = [0] * len(nums)
        suffixmin[-1] = nums[-1]
        prefixmax = nums[0]

        for idx in range(len(nums)-2, -1, -1):
            suffixmin[idx] = min(suffixmin[idx + 1], nums[idx])

        for idx in range(len(nums)):
            prefixmax = max(prefixmax, nums[idx])

            if prefixmax - suffixmin[idx] <= k:
                return idx
        return -1
            