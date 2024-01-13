"""
Rephrased Problem:
Given an array 'nums', count the number of subarrays where the first element is not larger than any other element in the subarray. A subarray is a contiguous part of the array.

Examples:
- Input: nums = [1,4,2,5,3]
  Output: 11
  Explanation: Valid subarrays are [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
- Input: nums = [3,2,1]
  Output: 3
  Explanation: Valid subarrays are [3],[2],[1].
- Input: nums = [2,2,2]
  Output: 6
  Explanation: Valid subarrays are [2],[2],[2],[2,2],[2,2],[2,2,2].

Solution with Inline Explanation:
"""

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []  # Stack to store elements in non-decreasing order
        res = 0  # Initialize result count

        for num in nums:
            # Pop elements from the stack if current num is smaller
            while stack and num < stack[-1]:
                stack.pop()

            # Add current num to the stack
            stack.append(num)

            # Increment result count by the current size of the stack
            # Each element in the stack contributes to a valid subarray ending at num
            res += len(stack)

        return res  # Return the total count of valid subarrays

# Example usage
sol = Solution()
print(sol.validSubarrays([1, 4, 2, 5, 3]))  # Output: 11
