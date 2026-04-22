class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_dict = {}
        longest_streak = 0
        tmp_streak = 0
        for letter in s:
            if letter in set_dict.keys():
                how_many_letters = len(set_dict[letter])
                tmp_streak = how_many_letters + 1
                if longest_streak < tmp_streak:
                    longest_streak = tmp_streak
                set_dict[letter] = set()

            else:
                set_dict[letter] = set()

            to_delete=set()
            for key in set_dict.keys():
                if key != letter:
                    if letter in set_dict[key]:
                        how_many_letters = len(set_dict[key])
                        tmp_streak = how_many_letters + 1
                        if longest_streak < tmp_streak:
                            longest_streak = tmp_streak
                        to_delete.add(key)
                    else:
                        set_dict[key].add(letter)
            for key in to_delete:
                set_dict.pop(key)
        longest_actual_streak = 0
        for value in set_dict.values():
            lng_tmp_streak = len(value) + 1
            if lng_tmp_streak > longest_actual_streak:
                longest_actual_streak = lng_tmp_streak
        return max(longest_streak, tmp_streak, longest_actual_streak)