class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        suffixmin = [nums[-1]]
        prefixmax = nums[0]
        min_idx = -1
        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] < suffixmin[0]:
                suffixmin.insert(0, nums[idx])
            else:
                suffixmin.insert(0, suffixmin[0])
        for idx in range(len(nums)):
            if nums[idx] > prefixmax:
                prefixmax = nums[idx]
            if prefixmax - suffixmin[idx] <= k:
                return idx
        return min_idx
            
        
