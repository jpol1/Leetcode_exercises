class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        longest_prefix = 0

        for num in arr1:
            while num and num not in prefixes:
                prefixes.add(num)
                num //= 10
        
        
        for num in arr2:
            while num and num not in prefixes:
                num //= 10
            if num:
                longest_prefix = max( len(str(num)), longest_prefix)
        
        return longest_prefix