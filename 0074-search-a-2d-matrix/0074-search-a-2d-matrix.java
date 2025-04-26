class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;

        int low = 0;
        int high = m - 1;

        while (low <= high) {
            int mid = getMidVal(low, high);
            int a = matrix[mid][0];
            int b = matrix[mid][n-1];
            if (target == a || target == b) {
                return true;
            } else if (a < target && target < b) {
                return binarySearch(matrix[mid], target);
            } else if (target < a) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return false;
    }

    public int getMidVal(int low, int high) {
        return (int) (low + (high - low)/2);
    }

    public boolean binarySearch(int[] arr, int target) {
        int n = arr.length;
        int low = 0;
        int high = n - 1;

        while (low <= high) {
            int mid = getMidVal(low, high);

            if (arr[mid] == target) {
                return true;
            }

            if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return false;
    }



}