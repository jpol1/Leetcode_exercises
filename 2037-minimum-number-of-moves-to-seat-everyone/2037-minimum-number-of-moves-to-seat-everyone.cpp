class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        int n = seats.size();
        int res = 0;
        std::sort(seats.begin(), seats.end());
        std::sort(students.begin(), students.end());
        for (int i = 0; i < n; i ++) {
            res += abs(seats[i] - students[i]);
        }
        return res;

        
    }
};