class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)

        max_range = 0
        for ele in num_set:
            if(ele-1 not in num_set):
                cur_range = 0
                while ele in num_set:
                    cur_range+=1
                    ele+=1
                if cur_range > max_range:
                    max_range = cur_range

        return max_range