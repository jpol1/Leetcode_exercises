class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int res = 0;
        for (int i: nums) {
            if (i%3 != 0) {
                res += 1;
            }
        }
        return res;
    }
};