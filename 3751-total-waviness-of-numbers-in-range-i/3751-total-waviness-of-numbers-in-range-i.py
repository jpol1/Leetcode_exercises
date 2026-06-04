class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        counter = 0
        for num in range(num1, num2+1):
            s = str(num)
            for idx in range(1, len(s)-1):
                if s[idx-1] < s[idx] > s[idx+1] or s[idx-1] > s[idx] < s[idx+1]:
                    counter += 1
        return counter