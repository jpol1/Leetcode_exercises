class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def find_minimum(start1, duration1, start2, duration2):
            finish1 = float("inf")
            for idx in range(len(start1)):
                finish1 = min(finish1, start1[idx] + duration1[idx])
            finish2 = float("inf")

            for idx in range(len(start2)):
                finish2 = min(finish2, max(finish1, start2[idx]) + duration2[idx])
            
            return finish2
        
        land_first = find_minimum(landStartTime, landDuration, waterStartTime, waterDuration)

        water_first = find_minimum(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_first, water_first)