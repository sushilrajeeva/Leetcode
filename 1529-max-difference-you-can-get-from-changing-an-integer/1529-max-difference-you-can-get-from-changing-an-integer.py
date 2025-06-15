class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # Make max number by replacing the first non-9 digit with 9
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # all 9s already

        # Make min number by replacing:
        # - first digit with 1 if it's not already 1
        # - or any other digit (not 0) with 0
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num

        return max_num - min_num
