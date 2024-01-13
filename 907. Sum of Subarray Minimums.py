
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = (10 ** 9) + 7  # Modulus for the final result
        stack = []  # Initialize a stack for indexes
        dp = [0] * len(arr)  # Dynamic programming array to store sum of minimums ending at each index

        # Iterate through each element in the array
        for i, n in enumerate(arr):
            # Pop elements from the stack while the current element is less than or equal to the element at the top of the stack
            while stack and arr[stack[-1]] >= n:
                stack.pop()

            # Calculate the sum of minimums for subarrays ending at index i
            if stack:
                # If the stack is not empty, the minimum for the current subarray ending at i
                # is the sum of minimums of the previous subarray plus the current element times the number of subarrays it can form
                dp[i] = dp[stack[-1]] + (n * (i - stack[-1]))
            else:
                # If the stack is empty, the minimum for the current subarray is the current element times its index plus one
                dp[i] = n * (i + 1)

            # Append the current index to the stack
            stack.append(i)

        # Return the sum of the dp array modulo mod
        return sum(dp) % mod
