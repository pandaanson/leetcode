class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        ans=0
        unseen=set([i for i in range(n)])
        def dfs(node):
             for neighbor in graph[node]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    dfs(neighbor)
        while unseen:
            ans+=1
            temp=unseen.pop()
            dfs(temp)
        return ans
