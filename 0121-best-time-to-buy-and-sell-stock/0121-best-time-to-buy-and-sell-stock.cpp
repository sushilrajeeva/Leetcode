#include <iostream>
#include <algorithm> // for std::max

using std::max;
using std::min;

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int profit = 0;

        int n = prices.size();

        if(n<=1){
            return 0;
        }

        int previous = prices[0];

        for(int i=0; i<n; i++){
            
            profit = max(profit, prices[i] - previous);
            previous = min(previous, prices[i]);
            
        }

        return profit;
        
    }
};