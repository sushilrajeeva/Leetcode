class Solution {
public:
    
    long getCoins(int num) {
        return (long)(num)*(num+1)/2;
    }

    int arrangeCoins(int n) {
        
        int left = 0;
        int right = n;

        while(left<=right){

            int mid = left + (right-left)/2;
            long coins = getCoins(mid);

            if(coins==n){
                return mid;
            }

            if(coins>n){
                right = mid - 1;
            }else{
                left = mid + 1;
            }


        }

        return right;

    }
};