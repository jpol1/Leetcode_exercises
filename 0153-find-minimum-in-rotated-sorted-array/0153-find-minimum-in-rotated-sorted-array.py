class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        min_elem = nums[mid]
        while(left <= right):
            mid = (left+right)//2
            if (nums[mid] < min_elem):
                min_elem = nums[mid]
            if (nums[right] < nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return min_elem