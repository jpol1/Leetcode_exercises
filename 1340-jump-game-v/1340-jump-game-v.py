class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = [None] * len(arr)
        max_path = 0 

        for start in range(len(arr)):
            best = 1

            def dfs(start):
                if memo[start]:
                    return memo[start]

                best = 1

                for i in range(1, d+1):
                    left = start - i
                    if left >= 0 and arr[start] > arr[left]:
                        best = max(best, 1 + dfs(left))
                    else:
                        break

                for i in range(1, d+1):
                    right = start + i
                    if right < len(arr) and arr[start] > arr[right]:
                        best = max(best, 1 + dfs(right))
                    else:
                        break
                
                memo[start] = best

                return best
            
            max_path = max(max_path, dfs(start))
        
        return max_path