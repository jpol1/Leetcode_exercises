class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for idx in range(n):
            if nums[idx] == nums[idx-1] and idx != 0:
                continue

            x = -1 * nums[idx]
            i, j = idx+1, n-1
            while(i < j):
                if nums[i] + nums[j] == x:
                    res.append([nums[idx], nums[i], nums[j]])
                    i+=1
                    j-=1
                    while(i < j and nums[i] == nums[i-1]):
                        i += 1
                    while (i < j and nums[j] == nums[j+1]):
                        j -= 1

                elif nums[i] + nums[j] < x:
                    i+=1
                else:
                    j-=1
        return res

