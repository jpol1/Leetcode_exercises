class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int sumRight = 0;
        int sumLeft = 0;

        vector<int> res;

        for (auto n: nums) {
            sumRight += n;
        }

        for (int i = 0; i<nums.size(); i ++) {
            sumRight -= nums[i];
            res.push_back(abs(sumRight - sumLeft));
            sumLeft += nums[i];
        }

        return res;
    }
};