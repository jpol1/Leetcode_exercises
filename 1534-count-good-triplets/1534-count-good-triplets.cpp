class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int size = static_cast<int>(arr.size());
        int result = 0, cond_a, cond_b, cond_c;
        for (int i = 0; i < size; i++) {
            for (int j = i+1; j < size; j++) {
                for(int k = j+1; k < size; k++) {
                    cond_a = abs(arr[i] - arr[j]);
                    cond_b = abs(arr[j] - arr[k]);
                    cond_c = abs(arr[i] - arr[k]);
                    if( cond_a <= a && cond_b <= b && cond_c <= c ) {
                        result += 1;
                    }
                }
            }
        }
        return result;
    }
};