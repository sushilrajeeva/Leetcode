class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for index, key in enumerate(nums):
            if hashmap.get(key, -1) != -1:
                if index - hashmap[key] <= k: return True
                else: hashmap[key] = index
            else:
                hashmap[key] = index
        return False
        