from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.length: int = 0
        self.all_combo_dict: Dict[str, List[str]] = defaultdict(list)

    def visitWordNode(
        self,
        queue: Deque[str],
        visited: Dict[str, int],
        others_visited: Dict[str, int],
    ) -> Any:
        queue_size: int = len(queue)
        for _ in range(queue_size):
            current_word: str = queue.popleft()
            for i in range(self.length):
                intermediate_word: str = (
                    current_word[:i] + "*" + current_word[i + 1 :]
                )

                for word in self.all_combo_dict[intermediate_word]:
             
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        visited[word] = visited[current_word] + 1
                        queue.append(word)

        return None

    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0

        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        queue_begin: Deque[str] = collections.deque(
            [beginWord]
        )  
        queue_end: Deque[str] = collections.deque(
            [endWord]
        )  
        visited_begin: Dict[str, int] = {beginWord: 1}
        visited_end: Dict[str, int] = {endWord: 1}
        ans: Any = None

        while queue_begin and queue_end:

            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(
                    queue_begin, visited_begin, visited_end
                )
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0