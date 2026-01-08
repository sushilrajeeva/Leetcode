class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self.lowbit(i)  # Move to the child node

    def query(self, i):
        total = 0
        while i > 0:
            total += self.sums[i]
            i -= self.lowbit(i)  # Move to the parent node
        return total

    @staticmethod
    def lowbit(x):
        return x & (-x)  # Equivalent to 2^k, where k is the position of the lowest set bit


class Solution:
    def reversePairs(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        doubled_nums = [2 * num for num in nums]
        sorted_set = sorted(set(nums).union(set(doubled_nums)))

        rank = 0
        ranks = {}

        for num in sorted_set:
            rank += 1
            ranks[num] = rank

        tree = FenwickTree(len(ranks))

        reverse_pairs_count = 0
        k = len(doubled_nums)
        for i in range(k - 1, -1, -1):
            reverse_pairs_count += tree.query(ranks[doubled_nums[i] // 2] - 1)
            tree.update(ranks[doubled_nums[i]], 1)

        return reverse_pairs_count