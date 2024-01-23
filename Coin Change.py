class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the memoization array with default values
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        # Bottom-up dynamic programming
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]
#top down
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the memoization array with default values
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0  # Base case: 0 coins are needed to make amount 0

        def dp(current):
            if current < 0:
                return float('inf')
            if memo[current] != float('inf'):
                return memo[current]

            # Compute the minimum coins needed for the current amount
            for coin in coins:
                test = dp(current - coin)
                if test != float('inf'):
                    memo[current] = min(memo[current], test + 1)
            return memo[current]

        result = dp(amount)
        return -1 if result == float('inf') else result

# Example usage
sol = Solution()
print(sol.coinChange([1,2,5], 11))  # Output: 3
print(sol.coinChange([2], 3))       # Output: -1
print(sol.coinChange([1], 0))       # Output: 0
