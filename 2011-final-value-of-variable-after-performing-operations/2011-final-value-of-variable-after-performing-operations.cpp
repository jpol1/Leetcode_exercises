class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for(string str:operations){
            for (char letter: str) {
                if (letter == '-') {
                    --x;
                    break;
                }
                else if (letter == '+') {
                    ++x;
                    break;
                }
            }
        }
        return x;
    }
};