class Solution:
    def check(self, nums: List[int]) -> bool:
        res = 0
        n = len(nums)

        for i in range(n):
            idx = (i+1) % n
            if nums[idx] < nums[idx-1]:
                res += 1

        if res <= 1 :
            return True
        return False
        