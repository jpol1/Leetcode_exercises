class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set()
        prohibited = set() #Lower letters
        special = set() # Upper letters
        for letter in word:
            if letter.islower():
                if letter.upper() in special:
                    prohibited.add(letter)
                    special.remove(letter.upper())
                else:
                    seen.add(letter)

            else:
                if letter.lower() not in seen:
                    prohibited.add(letter.lower())
                else:
                    if letter.lower() not in prohibited:
                        special.add(letter.upper())

        return len(special)