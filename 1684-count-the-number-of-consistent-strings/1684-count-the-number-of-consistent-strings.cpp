class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        std::unordered_set<char> letters(allowed.begin(), allowed.end());
        int res = 0;
        for (auto word: words) {
            bool flag = true;
            for (auto char_: word) {
                if (!letters.count(char_)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                res += 1;
            }
        }
        return res;
    }
};