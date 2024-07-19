class Solution {

    public int getTargetRow(int[][] matrix, int target){
        int left = 0;
        int right = matrix.length-1;
        while(left<=right){
            int mid = left + (right-left)/2;
            if(matrix[mid][0]==target){
                return mid;
            }
            if(matrix[mid][0]>target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }

        return right;
    }

    public boolean isPresentInRow(int[][] matrix, int target, int row){
        int left = 0;
        int right = matrix[0].length-1;
        while(left<=right){
            int mid = left + (right-left)/2;
            if(matrix[row][mid]==target){
                return true;
            }
            if(matrix[row][mid]>target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return false;
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false; // Handle empty matrix
        }
        int targetRow = getTargetRow(matrix, target);
        if (targetRow < 0 || targetRow >= matrix.length) {
            return false;
        }
        if (matrix[targetRow][0] <= target && target <= matrix[targetRow][matrix[0].length - 1]) {
            return isPresentInRow(matrix, target, targetRow);
        }

        return false;
    
    }
}