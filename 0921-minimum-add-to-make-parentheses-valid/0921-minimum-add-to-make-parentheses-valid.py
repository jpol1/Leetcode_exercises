class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        opens = {'(' , '{', '['}
        closes = {')': '(', '}':'{', ']':'['}
        for p in s:
            if p in opens:
                stack.append(p)
            elif p in closes:
                if len(stack) > 0 and stack[-1] == closes[p]:
                    stack.pop()
                else:
                    stack.append(p)
        return len(stack)
            
        