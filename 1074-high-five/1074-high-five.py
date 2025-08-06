import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        hashmap = dict()
        result = []

        for item in items:
            studentId, score = item
            if not studentId in hashmap:
                hashmap[studentId] = []
            
            heapq.heappush(hashmap[studentId], score)
            if len(hashmap[studentId]) > 5:
                heapq.heappop(hashmap[studentId])

        for key, value in hashmap.items():
            avg = sum(value)//len(value)
            result.append([key, avg])

        result.sort()

        return result

        


        