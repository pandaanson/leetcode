class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        Rephrased Problem:
        Find the total sum of the ranges of all contiguous subarrays of an array 'nums'. 
        The range of a subarray is defined as the difference between the largest and smallest elements in that subarray.

        Solution with Inline Explanation:
        """
        res = 0  # Initialize the result to store the sum of all ranges
        min_stack, max_stack = [], []  # Stacks to store indices for calculating min and max values
        n = len(nums)
        nums.append(0)  # Append a dummy element to handle edge cases
        
        # Iterate through each element in the array
        for i, num in enumerate(nums):
            # Calculate the contribution of the current element to the total sum as the minimum value
            while min_stack and (i == n or num < nums[min_stack[-1]]):
                top = min_stack.pop()
                starts = top - min_stack[-1] if min_stack else top + 1
                ends = i - top
                res -= starts * ends * nums[top]  # Subtract the contribution of this element as minimum

            # Push the current index onto the min_stack
            min_stack.append(i)

            # Calculate the contribution of the current element to the total sum as the maximum value
            while max_stack and (i == n or num > nums[max_stack[-1]]):
                top = max_stack.pop()
                starts = top - max_stack[-1] if max_stack else top + 1
                ends = i - top
                res += starts * ends * nums[top]  # Add the contribution of this element as maximum

            # Push the current index onto the max_stack
            max_stack.append(i)

        return res  # Return the total sum of ranges
