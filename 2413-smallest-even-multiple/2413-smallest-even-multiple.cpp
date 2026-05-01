class Solution {
public:
    int smallestEvenMultiple(int n) {
        int a = n, b = 2, r, nwd;
        while (b != 0) {
            r = a % b;
            a = b;
            b = r;
        }
            

        return (n*2)/a;
    }
};