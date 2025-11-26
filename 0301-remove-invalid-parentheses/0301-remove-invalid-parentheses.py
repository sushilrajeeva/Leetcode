from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest_str = -1
        self.res = set()

        self.dfs(s, 0, [], 0, 0)

        return list(self.res)

    def dfs(self, string: str, cur_idx: int, cur_res: List[str], l_count: int, r_count: int):
        # Base case: processed full string
        if cur_idx >= len(string):
            if l_count == r_count:
                cur_len = len(cur_res)
                if cur_len > self.longest_str:
                    self.longest_str = cur_len
                    self.res = set()
                    self.res.add("".join(cur_res))
                elif cur_len == self.longest_str:
                    self.res.add("".join(cur_res))
            return   # IMPORTANT: always stop here

        # Recursive case: still have characters to process
        cur_ch = string[cur_idx]

        if cur_ch == "(":
            # choose to keep '('
            cur_res.append(cur_ch)
            self.dfs(string, cur_idx + 1, cur_res, l_count + 1, r_count)
            cur_res.pop()

            # choose to skip '('
            self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)

        elif cur_ch == ")":
            # choose to skip ')'
            self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)

            # choose to keep ')' only if it won't make it invalid
            if l_count > r_count:
                cur_res.append(cur_ch)
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count + 1)
                cur_res.pop()

        else:
            # always keep non-parenthesis characters
            cur_res.append(cur_ch)
            self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
            cur_res.pop()
