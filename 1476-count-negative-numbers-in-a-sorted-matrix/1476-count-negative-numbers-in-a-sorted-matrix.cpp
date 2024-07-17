class Solution {
public:

    int getNegativesCount(vector<int>& row) {

        int n = row.size();
        int left = 0;
        int right = n-1;

        while(left<=right){
            int mid = left + (right - left)/2;

            if(row[mid]>=0){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }

        if(left >= n){
            return 0;
        }else{
            return n-left;
        }
        
    }

    int countNegatives(vector<vector<int>>& grid) {
        
        int count = 0;

        for(int i=0; i<grid.size(); i++){
            count += getNegativesCount(grid[i]);
        }

        return count;

    }
};