class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow: int = nums[0]
        fast: int = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        