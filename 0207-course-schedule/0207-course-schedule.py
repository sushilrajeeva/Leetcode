class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create adj matrix
        adj = [[] for _ in range(numCourses)]
        for preq in prerequisites:
            adj[preq[0]].append(preq[1])

        visited = [False] * numCourses
        pathVisited = [False] * numCourses

        def dfs(node: int) -> bool:

            if not visited[node]:
                visited[node] = True
                pathVisited[node] = True

                for neighbor in adj[node]:
                    if dfs(neighbor):
                        return True

            elif visited[node] and pathVisited[node]: return True

            pathVisited[node] = False

            return False

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        

        return True
        