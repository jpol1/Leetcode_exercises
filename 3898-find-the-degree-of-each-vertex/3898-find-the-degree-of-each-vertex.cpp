class Solution {
public:
    vector<int> findDegrees(vector<vector<int>>& matrix) {
        vector<int> res;
        for (int i = 0; i < matrix.size(); i++) {
            int tmp_res = 0;
            for (int j = 0; j<matrix[0].size(); j++) {
                tmp_res += matrix[i][j];
            }
            res.push_back(tmp_res);
        }
        return res;
    }
};