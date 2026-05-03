#include <unordered_set>

class Solution {
public:
    vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
        std::unordered_set<int> friends_set;
        vector<int> res;
        for(auto frnd: friends) {
            friends_set.insert(frnd);
        }
        for(auto ord: order) {
            if (friends_set.contains(ord)) {
                res.push_back(ord);
            }
        }

        return res;
    }
};