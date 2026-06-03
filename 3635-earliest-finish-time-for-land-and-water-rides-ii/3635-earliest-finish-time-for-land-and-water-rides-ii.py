class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def search_min(start1, duration1, start2, duration2):
            final1 = float('inf')
            for idx in range(len(start1)):
                final1 = min(start1[idx] + duration1[idx], final1)

            final2 = float('inf')
            for idx in range(len(start2)):
                final2 = min(final2, max(start2[idx], final1)+ duration2[idx])
            return final2
        
        return min(
            search_min(landStartTime, landDuration, waterStartTime, waterDuration),
            search_min(waterStartTime, waterDuration, landStartTime, landDuration),
        )