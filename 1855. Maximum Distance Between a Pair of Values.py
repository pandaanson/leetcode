class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Problem Statement:
        Given two non-increasing 0-indexed integer arrays nums1 and nums2,
        find the maximum distance between a pair of indices (i, j), where 0 <= i < len(nums1),
        0 <= j < len(nums2), i <= j, and nums1[i] <= nums2[j].
        The distance of the pair is defined as j - i. Return the maximum distance of any valid pair,
        or return 0 if no valid pairs exist.

        Example:
        nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
        Output: 2
        Explanation: The maximum distance is 2 with the valid pair (2,4).

        Solution Explanation:
        The solution uses two pointers to iterate through nums1 and nums2,
        finding the maximum distance for valid pairs.
        """

        length1, length2 = len(nums1), len(nums2)  # Lengths of nums1 and nums2
        i, j = 0, 0  # Pointers for nums1 and nums2

        result = 0  # Initialize the result to store the maximum distance

        # Iterate through nums1 and nums2
        while i < length1 and j < length2:
            # If nums1[i] is greater than nums2[j], increment i to find a smaller value in nums1
            if nums1[i] > nums2[j]:
                i += 1
            else:
                # If a valid pair is found, calculate the distance and update the result
                result = max(result, j - i)
                j += 1  # Increment j to explore further pairs

        return result
