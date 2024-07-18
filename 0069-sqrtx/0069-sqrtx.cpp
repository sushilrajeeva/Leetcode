class Solution {
public:
    int mySqrt(int x) {

        int left = 0;
        int right = 1 + (x/2);

        while(left<=right){

            int mid = left + (right-left)/2;
            double square = (double)mid*mid;

            if(square==x){
                return mid;
            }

            if(square<x){
                left = mid+1;
            }else{
                right = mid - 1;
            }

        }

        return right;
        
    }
};