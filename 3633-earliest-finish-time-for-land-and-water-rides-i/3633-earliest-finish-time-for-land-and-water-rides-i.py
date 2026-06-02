from math import factorial

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_res = float("inf")
        for land_idx in range(len(landStartTime)):
            for water_idx in range(len(waterStartTime)):
                land_end = landStartTime[land_idx] + landDuration[land_idx]
                water_end = waterStartTime[water_idx] + waterDuration[water_idx]
                
                if land_end >= waterStartTime[water_idx]:
                    min_res = min(land_end + waterDuration[water_idx], min_res)
                else:
                    diff = waterStartTime[water_idx] - land_end
                    min_res = min(land_end + diff + waterDuration[water_idx], min_res)

                if water_end >= landStartTime[land_idx]:
                    min_res = min(water_end + landDuration[land_idx], min_res)
                else:
                    diff = landStartTime[land_idx] - water_end
                    min_res = min(water_end + diff + landDuration[land_idx], min_res)

        return min_res


