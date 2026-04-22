class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        len_w = len(queries[0])
        res = []
        for idx, word in enumerate(queries):
            for dct in dictionary:
                counter = 0
                for letter in range(len_w):
                    if word[letter] != dct[letter]:
                        counter += 1
                        if counter > 2:
                            break
                res.append(queries[idx])
                break
        return res
        