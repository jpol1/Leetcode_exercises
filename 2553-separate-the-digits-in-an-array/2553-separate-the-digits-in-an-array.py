class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for number in nums:
            for digit in str(number):
                res.append(int(digit))
        return res
        