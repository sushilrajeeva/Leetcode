class Solution:
    
    def countSolders(self, arr: List[int]) -> int:
        count: int = 0
        for ele in arr:
            if ele != 1:
                return count
            count += 1
        return count
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        heap = []
        m: int = len(mat)
        n: int = len(mat[0])
            
        for i in range(m):
            row = mat[i]
            count = self.countSolders(row)
            heapq.heappush(heap, (count, i))
            
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
        
        
        
        