class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow: int = 0
        fast: int = 0
        n: int = len(nums)

        while fast < n:
            must_keep: bool = fast == 0 or nums[fast - 1] != nums[fast]
            if must_keep:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

        
        