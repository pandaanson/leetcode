from collections import deque 
# Given an array 'arr' of non-negative integers and a starting index 'start', determine if it is possible to reach an index in 'arr' where the value is 0.
# From any index 'i', you can jump to either 'i + arr[i]' or 'i - arr[i]'.
# You are not allowed to jump outside the bounds of the array.
# The function should return True if it's possible to reach an index with value 0, otherwise return False.

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        lenarr=len(arr)
        travelled=[False]*lenarr
        cue=deque()
        cue.append(start)
        while cue:
            temp=cue.popleft()
            if arr[temp]==0:return True
            travelled[temp]=True
            
            if temp+arr[temp]<lenarr and not travelled[temp+arr[temp]] :cue.append(temp+arr[temp])
            if temp-arr[temp]>=0 and not travelled[temp-arr[temp]]:cue.append(temp-arr[temp])
            

            
        return False
