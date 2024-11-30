from collections import defaultdict, deque
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Step 2: Find the starting node for the Eulerian path
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break

        # Step 3: Recursive DFS for Hierholzer's algorithm
        def dfs(node):
            while graph[node]:
                next_node = graph[node].popleft()
                dfs(next_node)
            euler_path.append(node)

        euler_path = []
        dfs(start_node)

        # Step 4: Format the result
        euler_path.reverse()
        return [[euler_path[i], euler_path[i + 1]] for i in range(len(euler_path) - 1)]