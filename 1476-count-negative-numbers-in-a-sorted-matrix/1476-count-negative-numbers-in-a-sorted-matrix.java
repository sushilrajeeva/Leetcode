class Solution {

    public int getNegativesCount(int[] row){
        int n = row.length;
        int left = 0; 
        int right = n-1;

        while(left<=right){
            int mid = left + (right-left)/2;

            if(row[mid]>=0){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }

        if(left>=n){
            return 0;
        }else{
            return n-left;
        }
    }

    public int countNegatives(int[][] grid) {

        int count = 0;

        for(int i=0; i<grid.length; i++){
            count += getNegativesCount(grid[i]);
        }

        return count;
        
    }
}