#include <map>
#include <unordered_set>
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        std::map<char, char> map, rmap;

        if (s.size() != t.size()) {
            return false;
        }
        for (int i = 0; i < s.size(); i++) {
            if (map.count(s[i])) {
                if (map[s[i]] != t[i] ) {
                    return false;
                }
            }
            else if(rmap.count(t[i])){
                if (map[t[i]] != s[i] ) {
                    return false;
                }
            }
            else {
                map[s[i]] = t[i];
                rmap[t[i]] = s[i];
            }
        }
        return true;
    }
};