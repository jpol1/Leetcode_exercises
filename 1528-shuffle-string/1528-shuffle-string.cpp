class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        std::string string_new(s.length(), '-');
        for (int i = 0; i < s.length(); i++) {
            string_new[indices[i]] = s[i];
        }
        return string_new;
    }
};