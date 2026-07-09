class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        components = [0]
        res = []
        com_number = 0
        for i in range(n-1):
            if nums[i+1] - nums[i] > maxDiff:
                com_number += 1
            components.append(com_number)


        for path in queries:
            if components[path[0]] == components[path[1]]:
                res.append(True)
            else:
                res.append(False)
        return res