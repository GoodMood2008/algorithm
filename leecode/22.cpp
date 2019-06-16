
#include <vector>
using namespace std:vector;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> results;
        backtrack(results, "", 0, 0, n);
        return results;
    }

private:
    void backtrack(vector<string>& results, const string result, int left, int right, int num) {
        if (left + right == num * 2) {
            results.add(result);
        }
        if (left < num) {
            backtrack(results, result + "(", left + 1, right, num);
        }
        if (right < left) {
            backtrack(results, result + ")", left, right + 1, num);
        } 
    }

};


int main(int argc, char* argv[])
{
    Solution solution;
    vector<string> result = solution.generateParenthesis(3);
    for (vector::iterator iter = result.begin(); iter != result.end(); ++iter) {
        std::cout << iter << std::endl;
    }
    return 0;
}