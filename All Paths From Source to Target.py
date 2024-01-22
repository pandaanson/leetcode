class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []  # List to store all valid paths

        def traveller(currentpoint, steps):
            # Create a new list for the current path
            temp = steps + [currentpoint]

            # Check if the current node is the target node
            if currentpoint == len(graph) - 1:
                ans.append(temp)
            else:
                # Recursively explore the next nodes in the graph
                for i in graph[currentpoint]:
                    traveller(i, temp)

        # Start the traversal from the source node (0)
        traveller(0, [])
        return ans
