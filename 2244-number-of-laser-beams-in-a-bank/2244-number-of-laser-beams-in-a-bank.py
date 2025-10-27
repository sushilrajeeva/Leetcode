class Solution:

    def getEdges(self, input: str) -> int:
        count: int = 0
        for e in input:
            if e == '1':
                count += 1
        return count

    def numberOfBeams(self, bank: List[str]) -> int:

        edges = 0
        
        for i in range(len(bank)):
            curRow = self.getEdges(bank[i])
            if curRow == 0: continue
            jRow = 0
            j = i+1
            while j < len(bank):
                jRow = self.getEdges(bank[j])
                j += 1
                if jRow > 0:
                    break

            edges += curRow * jRow
            
            

        return edges
            

        