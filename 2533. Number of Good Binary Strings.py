class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:

        MOD = 10**9 + 7

        dp = [0] * (maxLength + 1)
        dp[0] = 1

        for i in range(1, maxLength + 1):

            if oneGroup <= i:
                dp[i] += dp[i - oneGroup]
            

            if zeroGroup <= i:
                dp[i] += dp[i - zeroGroup]

        return sum(dp[minLength:]) % MOD
        
