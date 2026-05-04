class Solution {
public:
    int minBitFlips(int start, int goal) {
        int start_goal = start ^ goal;
        int res = 0;
        while (start_goal > 0) {
            res += start_goal & 1;
            start_goal >>= 1;
        }
        return res;
    }
};