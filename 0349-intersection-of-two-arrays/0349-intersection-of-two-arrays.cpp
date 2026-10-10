#include <vector>
#include <unordered_set>

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        std::unordered_set<int> set1(nums1.begin(), nums1.end()); //O(n)
        std::unordered_set<int> result; //O(1)
        for(int elem: nums2) { //O(m)
            if(set1.count(elem)){ //O(1)
                result.insert(elem); //O(1)
            }
        }
        return std::vector<int>(result.begin(), result.end()); //O(k)
    }
};
// n - Number of nums1 elements
// m - Number of nums2 elements
// k - unique elements of nums1 and nums2 intersection

//Time complexity: O(n+m)
//Memory complexity: O(n+m)