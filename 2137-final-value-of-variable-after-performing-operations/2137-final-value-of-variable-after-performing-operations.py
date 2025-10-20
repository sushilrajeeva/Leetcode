class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count: int = 0
        for operation in operations:
            if operation.startswith('-') or operation.endswith('-'):
                count -= 1
            else:
                count += 1
        return count
        