class Solution:

    def carsRepaired(self, rank: int, time: int) -> int:
        return int(math.sqrt(time/rank))

    def canSolveInTime(self, ranks: List[int], time: int, cars: int) -> bool:
        total_repaired = 0
        for rank in ranks:
            total_repaired += self.carsRepaired(rank, time)
            if total_repaired >= cars:
                return True
        return total_repaired >= cars
        

    def repairCars(self, ranks: List[int], cars: int) -> int:
        left: int = 0
        right: int = max(ranks) * cars * cars
        answer: int = right

        while left <= right:
            mid: int = left + (right - left)//2
            if self.canSolveInTime(ranks, mid, cars):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer