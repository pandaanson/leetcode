class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        temp1=dict()
        temp2=dict()
        temp=nums.pop()
        # Initialize temp1 with the first number
        temp1[temp] = temp1.get(temp, 0) + 1
        temp1[-temp] = temp1.get(-temp, 0) + 1

        while nums:
            temp = nums.pop()
            temp2.clear()  # Clear temp2 for the new iteration
            for i in temp1:
                temp2[i + temp] = temp2.get(i + temp, 0) + temp1[i]
                temp2[i - temp] = temp2.get(i - temp, 0) + temp1[i]
            temp1 = temp2.copy()  # Copy temp2 to temp1 for the next iteration

        return temp1.get(target, 0)
