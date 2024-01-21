class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)
        mid=(left+right)//2
        while left<right-1:
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid
            mid=(left+right)//2
        return -1
