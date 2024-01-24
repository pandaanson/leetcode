class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Calculate the max money that can be robbed, excluding either the first or last house
        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        # Helper function to rob a linear arrangement of houses
        t1 = 0  # Max money robbed till the previous house
        t2 = 0  # Max money robbed till the house before the previous house
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)  # Rob current house or skip it
            t2 = temp

        return t1


