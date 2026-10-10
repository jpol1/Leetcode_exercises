#include <unordered_map>
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        std::unordered_map<char, char> map, rmap; //O(1)

        if (s.size() != t.size()) { //O(1)
            return false;
        }
        for (int i = 0; i < s.size(); i++) { //O(n)
            if (map.count(s[i])) { //O(1)
                if (map[s[i]] != t[i] ) { //O(1)
                    return false; //O(1)
                }
            }
            else if(rmap.count(t[i])){ //O(1)
                if (rmap[t[i]] != s[i] ) { //O(1)
                    return false; //O(1)
                }
            }
            else {
                map[s[i]] = t[i];//O(1)
                rmap[t[i]] = s[i];//O(1)
            }
        }
        return true; //O(1)
    }
};

// n - length of the strings
// k - number of distinct characters
// Time complexity: O(n)
// Space complexity: O(k)