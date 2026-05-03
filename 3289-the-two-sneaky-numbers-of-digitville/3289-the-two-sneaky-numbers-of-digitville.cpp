#include <unordered_set>

class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_set<int> appearance;
        vector<int> res;
        for (auto n: nums) {
            if(appearance.contains(n)) {
                res.push_back(n);
            }
            else {
                appearance.insert(n);
            }
        }
        return res;
    }
};