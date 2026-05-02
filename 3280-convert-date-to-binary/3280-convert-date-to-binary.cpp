long int bit_number(int number) {
    long int res = 0;
    int multiplier = 0;
    while (number > 0) {
        res = res + ((number % 2) * pow(10,multiplier));
        multiplier++;
        number /= 2;
    }
    return res;
}

class Solution {
public:
    string convertDateToBinary(string date) {
        int year = std::stoi(date.substr(0,4));
        int month = std::stoi(date.substr(5,2));
        int day = std::stoi(date.substr(8));
        return std::to_string(bit_number(year)) + "-" + std::to_string(bit_number(month)) + "-" + std::to_string(bit_number(day));
    }
};