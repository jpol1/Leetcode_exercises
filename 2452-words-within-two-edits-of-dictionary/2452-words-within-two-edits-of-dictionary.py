class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        len_w = len(queries[0])
        res = []
        for word in queries:
            for dct in dictionary:
                counter = 0
                for letter_w, letter_d in zip(word, dct):
                    if letter_w != letter_d:
                        counter += 1
                        if counter > 2:
                            break
                else:            
                    res.append(word)
                    break
        return res
        