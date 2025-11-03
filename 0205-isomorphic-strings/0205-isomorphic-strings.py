class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapper_st = {}
        mapper_ts = {}

        for c1, c2 in zip(s, t):

            if (c1 not in mapper_st) and (c2 not in mapper_ts):
                mapper_st[c1] = c2
                mapper_ts[c2] = c1

            elif mapper_st.get(c1) != c2 or mapper_ts.get(c2) != c1:
                return False

        return True


        