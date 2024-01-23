class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Problem Statement:
        Given a string 's', partition 's' into substrings such that each substring is a palindrome.
        Return all possible palindrome partitioning of 's'.

        Example:
        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]
        Explanation: There are two partitions of "aab" where each substring is a palindrome.

        Solution Explanation:
        The solution uses depth-first search (DFS) to explore all possible partitions
        and a helper function to check if a string is a palindrome.
        """

        lst = []  # List to store all palindrome partitions

        def palindrome(a):
            # Check if a string 'a' is a palindrome
            return a == a[::-1]

        def dfs(i, curr):
            # If 'i' reaches the end of 's', add the current partition to 'lst'
            if i == len(s):
                lst.append(curr)
                return
            
            # Explore all possible partitions starting from index 'i'
            for j in range(i, len(s)):
                sol = s[i:j + 1]  # Extract the substring from 'i' to 'j'
                # If the substring is a palindrome, continue partitioning the rest of the string
                if palindrome(sol):
                    dfs(j + 1, curr + [sol])

        dfs(0, [])  # Start DFS with an empty partition
        return lst
