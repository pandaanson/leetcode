class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        Given an array 'nums' and an integer 'k', the task is to modify the array up to 'k' times by 
        choosing an index 'i' and replacing 'nums[i]' with '-nums[i]'. This operation can be performed 
        on the same index multiple times. The goal is to return the largest possible sum of the array 
        after these modifications.
        """
        
        # First, sort the array to prioritize negating negative numbers
        nums.sort()

        # Negate negative numbers as long as 'k' allows
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # If 'k' is still positive and odd, negate the smallest element
        if k % 2 == 1:
            nums.sort()  # Resort the array to find the smallest element
            nums[0] = -nums[0]

        # Return the sum of the modified array
        return sum(nums)
