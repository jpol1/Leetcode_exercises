class Solution {
public:
    string reversePrefix(string word, char ch) {
        int idx = word.find(ch);
        for (int i = 0; i < (idx+1)/2; i++) {
            char tmp_char = word[i];
            word[i] = word[idx-i];
            word[idx-i] = tmp_char;
        }
        return word;
    }
};