class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        Given an integer array 'nums' and an integer 'm', split 'nums' into 'm' non-empty subarrays such that
        the largest sum of any subarray is minimized. Return the minimized largest sum of the split.
        A subarray is a contiguous part of the array.
        """

        # Function to check if it's possible to split the array into 'm' subarrays
        # such that the largest sum of any subarray does not exceed 'max_sum'
        def cannot_split(max_sum, m):
            cuts, curr_sum  = 0, 0
            for x in nums:
                curr_sum += x
                # If current sum exceeds 'max_sum', make a cut and start a new subarray
                if curr_sum > max_sum:
                    cuts += 1
                    curr_sum = x
            # Total number of subarrays needed
            subs = cuts + 1
            # Return True if more than 'm' subarrays are needed, False otherwise
            return (subs > m)
        
        # Set initial search range for binary search
        # 'low' is the maximum single element, 'high' is the sum of all elements
        low, high = max(nums), sum(nums)
        # Binary search to find the minimum largest sum
        while low < high:
            guess = low + (high - low) // 2
            # If the guessed sum requires more than 'm' subarrays, increase the guessed sum
            if cannot_split(guess, m):
                low = guess + 1
            # Otherwise, try a smaller guessed sum
            else:
                high = guess
        # The smallest sum that allows splitting into 'm' subarrays
        return low

# Example usage
# sol = Solution()
# print(sol.splitArray(nums, m))
