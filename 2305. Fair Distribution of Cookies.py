class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
        Problem Statement:
        Given an array 'cookies' where cookies[i] represents the number of cookies in the ith bag,
        and an integer 'k' representing the number of children, distribute the cookies among the children.
        The goal is to minimize the unfairness, defined as the maximum total number of cookies received
        by any single child. Return the minimum possible unfairness.

        Example:
        Input: cookies = [8,15,10,20,8], k = 2
        Output: 31
        Explanation: One optimal way to distribute is [8,15,8] to one child and [10,20] to another.
                     The maximum cookies any child gets is 31, which is the minimum unfairness possible.

        Solution Explanation:
        The solution uses depth-first search (DFS) to explore all possible ways of distributing cookies.
        """

        def dfs(p):
            nonlocal best  # Reference the variable 'best' defined in the outer scope
            if p == len(cookies):
                # Update the minimum unfairness after all cookies are distributed
                best = min(best, max(split))
                return
            
            # Distribute the current bag of cookies to a new child if possible
            if len(split) < k:
                split.append(cookies[p])
                dfs(p + 1)
                split.pop()  # Backtrack

            # Distribute the current bag of cookies to a child who already has cookies
            for i in range(len(split)):
                if split[i] + cookies[p] < best:
                    split[i] += cookies[p]
                    dfs(p + 1)
                    split[i] -= cookies[p]  # Backtrack

        split = []  # List to track the cookies each child gets
        best = float("inf")  # Initialize the minimum unfairness
        dfs(0)  # Start the DFS
        return best
