class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # same as finding ceil

        n = len(letters)
        left, right = 0, n-1

        while left<=right:

            mid = left + (right-left)//2

            if ord(letters[mid]) <= ord(target):
                # move right
                left = mid + 1
            else:
                right = mid - 1

        return letters[left%n]