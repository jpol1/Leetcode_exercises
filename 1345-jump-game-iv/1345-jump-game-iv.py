class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idx_val = {}
        n = len(arr)
        for idx, val in enumerate(arr):
            if (val in idx_val):
                idx_val[val].append(idx)
            else:
                idx_val[val] = [idx]

        queue = [0]
        length = 0

        visited = set()
        while (queue):
            level_counter = len(queue)

            for i in range(level_counter):
                idx = queue[i]
                if idx < 0 or idx >= n or idx in visited:
                    continue

                visited.add(idx)
                if idx == n-1:
                    return length
                else:
                    queue.append(idx-1)
                    queue.append(idx+1)
                    arr_extend = idx_val.get(arr[idx], None)
                    if arr != None:
                        queue.extend(arr_extend)
                        idx_val[arr[idx]] = []

            length += 1
            queue = queue[level_counter:]

        return n - 1