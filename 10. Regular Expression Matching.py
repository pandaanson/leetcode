class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        
        # Initialize dp table where dp[i][j] will be True if s[0..i-1] matches p[0..j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # An empty pattern matches an empty string
        dp[0][0] = True
        
        # Initialize the first row for the cases where pattern p can match an empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Iterate through the dp table to fill it
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # If characters match, or pattern has a '.', copy diagonal value
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                
                # If pattern has '*', two scenarios: zero occurrence or one/more occurrences
                elif p[j - 1] == '*':
                    
                    # Zero occurrence case, copy value two columns back
                    dp[i][j] = dp[i][j - 2]
                    
                    # One or more occurrence case, copy value from the same column one row up
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        # Return True or False based on the last cell which considers the entire string and pattern
        return dp[m][n]
