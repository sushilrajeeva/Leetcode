class Solution:

    def intersection(self, interval1: List[int], interval2: List[int]) -> List[int]:
        overlap_start: int = max(interval1[0], interval2[0])
        overlap_end: int = min(interval1[1], interval2[1])
        return [overlap_start, overlap_end]

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        p1: int = 0
        p2: int = 0

        n1: int = len(firstList)
        n2: int = len(secondList)

        result: List[List[int]] = []

        while p1 < n1 and p2 < n2:
            interval1: List[int] = firstList[p1]
            interval2: List[int] = secondList[p2]

            if interval1[1] < interval2[0]:
                p1 += 1
            elif interval2[1] < interval1[0]:
                p2 += 1
            else:
                result.append(self.intersection(interval1, interval2))
                if interval1[1] < interval2[1]:
                    p1 += 1
                else:
                    p2 += 1
                    
        return result

        