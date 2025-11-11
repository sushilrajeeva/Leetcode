class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False

        signature1 = [0] * 26
        signature2 = [0] * 26
        for i in range(m):
            signature1[ord(s1[i]) - 97] += 1
            signature2[ord(s2[i]) - 97] += 1
        
        left = 0
        right = m - 1

        while right < n:
            if signature1 == signature2: return True
            if right == n-1: break
            signature2[ord(s2[left]) - 97] -= 1
            left += 1
            right += 1
            signature2[ord(s2[right]) - 97] += 1

        return False


        