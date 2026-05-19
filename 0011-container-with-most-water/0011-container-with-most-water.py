class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_container = 0
        while (i < j):
            container_count = min(height[i], height[j])*(j-i)
            max_container = max(container_count, max_container)
            
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_container
