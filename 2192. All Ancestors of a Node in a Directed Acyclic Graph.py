class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        2192. All Ancestors of a Node in a Directed Acyclic Graph
        Given a positive integer n representing the number of nodes in a Directed Acyclic Graph (DAG),
        and a 2D integer array edges where edges[i] = [fromi, toi] indicates a unidirectional edge from fromi to toi,
        return a list where each element is a list of ancestors of the ith node, sorted in ascending order.
        A node u is an ancestor of another node v if u can reach v via a set of edges.
        """

        # Initialize the visited array and adjacency list
        visited = [False] * n
        tothatpoint = [[] for _ in range(n)]
        for i, j in edges:
            tothatpoint[j].append(i)

        # Define a DFS helper function
        def dfs(node):
            if visited[node]:
                return ancestors[node]
            visited[node] = True
            ans = set()
            for parent in tothatpoint[node]:
                ans.update(dfs(parent))
                ans.add(parent)
            ancestors[node] = ans
            return ans

        # Initialize the ancestors array
        ancestors = [set() for _ in range(n)]

        # Perform DFS for each node
        for i in range(n):
            dfs(i)

        # Convert each set of ancestors to a sorted list
        return [sorted(list(anc)) for anc in ancestors]

# Example usage
# sol = Solution()
# print(sol.getAncestors(n, edges))
