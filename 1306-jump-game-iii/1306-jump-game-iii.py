class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = set()
        max_idx = len(arr) - 1
        while stack:
            idx = stack.pop()
            if (idx < 0 or idx > max_idx or idx in visited):
                continue
            
            if arr[idx] == 0:
                return True
            
            stack.append(idx-arr[idx])
            stack.append(idx+arr[idx])
            visited.add(idx)
        return False