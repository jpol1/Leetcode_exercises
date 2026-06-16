class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for letter in s:
            if letter.isalpha() and letter.islower():
                result.append(letter)
            elif letter == "#":
                result.extend(result)
            elif letter == "*" and result:
                result.pop()
            elif letter == "%" and result:
                result.reverse()
        return "".join(result)

