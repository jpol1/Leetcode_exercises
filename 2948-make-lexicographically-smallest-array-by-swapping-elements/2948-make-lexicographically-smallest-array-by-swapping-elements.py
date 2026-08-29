class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        pairs = sorted((num, idx) for idx, num in enumerate(nums))
        current_group = [pairs[0]]

        for i in range(1, len(pairs)):
            if pairs[i][0] - pairs[i-1][0] <= limit:
                current_group.append(pairs[i])
            else:
                idxes = sorted(pair[1] for pair in current_group)

                for j in range(len(current_group)):
                    nums[idxes[j]] = current_group[j][0]

                current_group = [pairs[i]]

        idxes = sorted(pair[1] for pair in current_group)

        for j in range(len(current_group)):
            nums[idxes[j]] = current_group[j][0]
        return nums


            
                
