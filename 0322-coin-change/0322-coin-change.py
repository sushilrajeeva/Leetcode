from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        queue = deque([(0, 0)]) # (cur_sum, cur_total)
        visited = {0}

        while queue:
            cur_sum, cur_total = queue.popleft()
            if cur_sum == amount:
                return cur_total
            
            for coin in coins:
                _sum = cur_sum + coin
                if _sum <= amount and _sum not in visited:
                    visited.add(_sum)
                    queue.append((_sum, cur_total + 1))
        
        return -1
                    

        