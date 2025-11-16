class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort() 
        originally_complete = sum(flowers[i] >= target for i in range(n))
        work_end = n - originally_complete
        # [0,        j-1] — incomplete (with >=`level` flowers each, where `0 <= `level` <= target - 1) 
        # [j, work_end-1] — complete
        # [work_end, n-1] — originally complete

        i = -1
        level = 0
        def maximize_min_number_of_flowers() -> None:
            nonlocal i, level, newFlowers
            if j == 0:
                return
            if i == -1:
                i = 0
                level = flowers[0]
            while i < j:
                next_level = flowers[i+1] if i + 1 < j else target - 1
                max_boost = min(next_level - level, newFlowers // (i+1))
                level += max_boost
                newFlowers -= max_boost * (i+1)
                if level != next_level:
                    break
                i += 1
        
        j = work_end
        def add_complete_garden() -> bool:
            nonlocal j, newFlowers
            if j - 1 < 0 or newFlowers < target - flowers[j-1]:
                return False
            newFlowers -= target - flowers[j-1]
            j -= 1
            return True
        def remove_complete_garden() -> None:
            nonlocal j, newFlowers
            assert j < work_end
            newFlowers += target - flowers[j]
            flowers[j] = flowers[j]
            j += 1

        while add_complete_garden():
            pass
        maximize_min_number_of_flowers()
        ans = full * (n - j) + partial * level
        while j < work_end:
            remove_complete_garden()
            maximize_min_number_of_flowers()
            ans = max(ans, full * (n - j) + partial * level)
        return ans