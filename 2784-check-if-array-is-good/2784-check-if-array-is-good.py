class Solution:
    def isGood(self, nums: List[int]) -> bool:
        dct_counter = {}
        max_el = max(nums)
        for num in nums:
            if num not in dct_counter:
                dct_counter[num] = 1
            else:
                dct_counter[num] += 1
        dct_counter = sorted(dct_counter.items(), key=lambda x: x[1], reverse=True)
        if len(nums) != max_el+1:
            return False
        if dct_counter[0][0] != max_el:
            return False
        if dct_counter[0][1] != 2:
            return False
        if len(dct_counter) > 1 and (dct_counter[1][1] > 1):
            return False
        return True
