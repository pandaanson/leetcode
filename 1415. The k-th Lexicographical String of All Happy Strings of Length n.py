class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(n, last_char, happystring): 
            nonlocal count
            if n == 0:
                count += 1
                if count == k:
                    ans.append(happystring)
                return
            for char in ['a', 'b', 'c']:
                if last_char != char:
                    dfs(n - 1, char, happystring + char)

        ans = []
        count = 0
        dfs(n, '', '')  # Start DFS with an empty last character and empty happystring
        return ans[0] if ans else ""
