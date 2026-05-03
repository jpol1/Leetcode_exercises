#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int maxFreqSum(string s) {
        std::unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        std::unordered_map<char, int> vowels_cnt;
        std::unordered_map<char, int> consonant_cnt;
        int max_vowel = 0;
        int max_consonant = 0;
        for (char letter: s) {
            if (vowels.contains(letter)) {
                if(vowels_cnt.contains(letter)) {
                    vowels_cnt[letter]++;
                }
                else {
                    vowels_cnt[letter] = 1;
                }
            }
            else {
                if(consonant_cnt.contains(letter)) {
                    consonant_cnt[letter]++;
                }
                else {
                    consonant_cnt[letter] = 1;
                }
            }
        }

        for (auto pair: vowels_cnt) {
            if (pair.second > max_vowel) {
                max_vowel = pair.second;
            }
        }

        for (auto pair: consonant_cnt) {
            if (pair.second > max_consonant) {
                max_consonant = pair.second;
            }
        }
        return max_consonant + max_vowel;

    }
};