class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set()
        special = set()
        for letter in word:
            opposite = letter.lower() if letter.isupper() else letter.upper()
            if opposite in seen:
                special.add(letter.lower())
            seen.add(letter)
        return len(special)
        