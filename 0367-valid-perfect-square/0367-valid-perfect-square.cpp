class Solution {
public:
    bool isPerfectSquare(int num) {

        if(num==1){
            return true;
        }

        int left = 0;
        int right = num;

        while(left<=right){
            
            int mid = left + (right-left)/2;

            double square = (double)mid * mid;

            if(square==num){
                return true;
            }

            if(square<num){
                left = mid+1;
            }else{
                right = mid-1;
            }

        }

        return false;
        
    }
};