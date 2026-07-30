class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        res = 0
        costs = {1: set(), 2: set(), 3: set(), 4: set()}
        for letter in word:
            if letter in costs[1] or len(costs[1]) < 8:
                res += 1
                costs[1].add(letter)
            elif letter in costs[2] or len(costs[2]) < 8:
                res += 2
                costs[2].add(letter)
            elif letter in costs[3] or len(costs[3]) < 8:
                res += 3
                costs[3].add(letter)
            else:
                res += 4
                costs[4].add(letter)
        return res