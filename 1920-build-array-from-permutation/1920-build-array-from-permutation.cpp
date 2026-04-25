class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> res;
        for (auto n: nums){
            res.emplace_back(nums[n]);
        }
        return res;
    }
};