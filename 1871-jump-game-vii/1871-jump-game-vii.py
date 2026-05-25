class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        farthest_checked = 0
        queue = [0]
        ls = len(s)
        while (queue):
            n = len(queue)
            for idx in range(n):
                if queue[idx] == ls - 1:
                    return True
                start = max(minJump+queue[idx], farthest_checked+1)
                end = queue[idx] + maxJump + 1
                for jump in range(start, end):
                    if jump < ls and s[jump] == "0":
                        queue.append(jump)
                farthest_checked = end - 1
            queue = queue[n:]
        return False