import heapq
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDif = None

        dic = dict()
        arr_heap = []

        for ele in arr:
            heapq.heappush(arr_heap, ele)
        

        while arr_heap:
            print("hi")
            x = heapq.heappop(arr_heap)
            if not arr_heap:
                break
            y = arr_heap[0]

            z = y - x

            if not minDif:
                minDif = z
            if z <= minDif:
                minDif = z
                if not dic.get(z, None):
                    dic[z] = []
                dic[z].append([x, y])
        
        return dic[minDif] if dic.get(minDif, None) else []




        