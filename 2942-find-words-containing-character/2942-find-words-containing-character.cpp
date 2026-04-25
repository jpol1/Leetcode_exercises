class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> res;
        for(int i = 0; i < words.size(); i++) {
            for(int l = 0; l < words[i].size(); l++) {
                if (words[i][l] == x) {
                    res.push_back(i);
                    break;
                }
            }
        }
        return res;
    }
};