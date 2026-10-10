#include <vector>
#include <unordered_set>

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        std::unordered_set<int> set1(nums1.begin(), nums1.end());
        std::unordered_set<int> result;
        for(int elem: nums2) {
            if(set1.count(elem)){
                result.insert(elem);
            }
        }
        return std::vector<int>(result.begin(), result.end());
    }
};