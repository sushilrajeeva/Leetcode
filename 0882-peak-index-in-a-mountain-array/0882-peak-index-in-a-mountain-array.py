class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        n = len(arr)
        left = 0
        right = n-1

        # edge case
        if arr[0]>arr[1]:
            return 0
        elif arr[right]>arr[right-1]:
            return right

        while left <= right:
            mid = left + (right-left)//2

            if(mid > 0 and mid < n-1 and arr[mid-1] < arr[mid] and arr[mid] > arr[mid + 1]):
                return mid
            
            if (mid %2 == 0 and arr[mid] <= arr[mid+1]) or (mid %2 == 1 and arr[mid-1] <= arr[mid]):
                left = mid + 1
            else:
                right = mid - 1

        return left

        