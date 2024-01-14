#Consider an undirected tree consisting of n nodes labeled from 0 to n - 1, connected by n - 1 edges. You are provided with a 2D integer array edges of size n - 1, where each element edges[i] = [ai, bi] signifies an edge connecting nodes ai and bi. Additionally, you are given an integer array restricted containing the labels of nodes that are restricted. Determine the maximum number of nodes that can be reached from node 0, ensuring that none of the visited nodes are restricted. It is given that node 0 is not a restricted node.
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted=set(restricted)
        graph = defaultdict(list)
        for x, y in edges:
            if x not in restricted and y not in restricted:
                graph[x].append(y)
                graph[y].append(x)
        
        seen=set([0])
        def dfs(node):
            nonlocal ans
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    ans+=1
                    dfs(neighbor)
        ans=1
        dfs(0)
        return ans
        
        
