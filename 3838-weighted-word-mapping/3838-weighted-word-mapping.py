import string
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res_string = ""
        alphabet = string.ascii_lowercase
        n = len(alphabet)
        alphabet_dct = {letter: idx for idx, letter in enumerate(alphabet)}
        for word in words:
            search = 0
            for letter in word:
                search += weights[alphabet_dct[letter]]
            mod = search%26
            res_string += alphabet[n-mod-1]
        return res_string

