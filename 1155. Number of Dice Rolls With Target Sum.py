class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: 0 ways to get any sum with 0 dice

        # Iterate for each dice
        for _ in range(n):
            temp = dp.copy()
            dp = [0] * (target + 1)
            # Update dp for each possible sum
            for i in range(target + 1):
                # Consider all faces of the dice
                for dice in range(1, k + 1):
                    if i + dice <= target:
                        dp[i + dice] = (dp[i + dice] + temp[i]) % MOD

        return dp[target]
