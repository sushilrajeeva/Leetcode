class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        visited = [False] * numCourses
        pathVisited = [False] * numCourses
        adj = [[] for _ in range(numCourses)]
        courseOrder = []


        for preq in prerequisites:
            adj[preq[0]].append(preq[1])

        def dfs(node: int) -> bool:
            
            if not visited[node]:
                visited[node] = True
                pathVisited[node] = True

                for neighbor in adj[node]:
                    if dfs(neighbor):
                        return True
                courseOrder.append(node)

            elif visited[node] and pathVisited[node]: return True

            pathVisited[node] = False
            

            return False

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
        
        return courseOrder
        