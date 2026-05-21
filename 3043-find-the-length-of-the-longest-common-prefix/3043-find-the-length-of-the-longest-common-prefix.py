class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        longest_prefix = 0

        for num in arr1:
            num_str = str(num)
            for idx in range(1, len(num_str)+1):
                prefixes.add(num_str[:idx])
        
        for num in arr2:
            num_str = str(num)
            for idx in range(1, len(num_str)+1):
                if num_str[:idx] in prefixes:
                    if idx > longest_prefix:
                        longest_prefix = idx
        
        return longest_prefix