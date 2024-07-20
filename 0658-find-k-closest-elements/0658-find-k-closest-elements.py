import heapq

class Solution:

    def isClosest(self, a: int, b: int, x: int) -> bool:
        if abs(a-x) < abs(b-x) or (abs(a-x) == abs(b-x) and a<b):
            return True
        return False

    def closestIndex(self, arr: List[int], target: int) -> int:

        n = len(arr)
        left = 0
        right = n-1

        while left<=right:
            mid = left + (right-left)//2

            
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if right < 0:
            return left
        if left >= n:
            return right

        if arr[right] == target or (abs(arr[right]-target) < abs(arr[right+1]-target)) or (abs(arr[right]-target) == abs(arr[right+1]-target) and arr[right] < arr[right+1]):
            return right
        return left

        

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        # edge case:
        if n == 1:
            return arr
        if k == n:
            return arr

        if x <= arr[0]:
            return arr[:k]

        if x >= arr[-1]:
            return arr[-k:]

        closestIndex = self.closestIndex(arr, x)

        left, right = closestIndex, closestIndex + 1

        result = []
        heapq.heapify(result)
        count = 0
        while count<k and (left >= 0 or right < n):

            if left >= 0 and (right >= n or self.isClosest(arr[left], arr[right], x)):
                heapq.heappush(result, arr[left])
                left -= 1
            else:
                heapq.heappush(result, arr[right])
                right += 1

            count += 1

        output = []
        while count!=0:
            output.append(heapq.heappop(result))
            count-=1

        return output

        
                



        