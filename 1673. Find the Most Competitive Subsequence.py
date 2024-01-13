class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        Given an array 'nums' and an integer 'k', find the most competitive subsequence of length 'k'.
        A subsequence is most competitive if it is the smallest lexicographically among all subsequences
        of the same length.

        The function returns the most competitive subsequence as a list.
        """
        st = []  # Stack to build the most competitive subsequence

        # Iterate over each element in nums
        for idx, num in enumerate(nums):
            # If stack is empty, append the current element
            if not st:
                st.append(num)
            else:
                # While conditions are met, pop from the stack
                while st and st[-1] > num and (len(st) - 1 + len(nums) - idx >= k):
                    st.pop()
                # Append current element if stack size is less than k
                if len(st) < k:
                    st.append(num)

        return st  # Return the most competitive subsequence

# Example usage
sol = Solution()
print(sol.mostCompetitive([3, 5, 2, 6], 2))  # Output: [2, 6]
