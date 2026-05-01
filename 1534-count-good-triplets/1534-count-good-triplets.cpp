class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int32_t size = static_cast<int32_t>(arr.size());
        int32_t result = 0, cond_a, cond_b, cond_c;
        for (int32_t i = 0; i < size; i++) {
            for (int32_t j = i+1; j < size; j++) {
                for(int32_t k = j+1; k < size; k) {
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