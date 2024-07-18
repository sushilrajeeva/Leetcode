#include <iostream>
#include <algorithm>

using std::max;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        int n = nums.size();

        if(n==0){
            return 0;
        }

        int path = nums[0];
        int maxSum = nums[0];

        for(int i=1; i<n; i++){
            path = max(path+nums[i], nums[i]);
            maxSum = max(maxSum, path);
        }
        
        return maxSum;
    }
};