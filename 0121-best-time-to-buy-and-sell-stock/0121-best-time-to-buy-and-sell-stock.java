import java.lang.Math;

class Solution {
    public int maxProfit(int[] prices) {

        int profit = 0;
        int n = prices.length;

        if(n<=1){
            return 0;
        }

        int previous = prices[0];
        
        for(int i=0; i<n; i++){
            profit = Math.max(profit, prices[i]-previous);
            previous = Math.min(previous, prices[i]);
            
        }

        return profit;

    }
}