class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        lenh=len(heights)
        ans=[0]*lenh
        stack=[]
        for i in range(lenh-1,-1,-1):

                
            while stack and stack[-1]<heights[i]:
                stack.pop()
                ans[i]+=1
            if stack:
                ans[i]+=1
            stack.append(heights[i])
        return ans
