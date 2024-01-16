class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans=0
        allow=5000
        for i in weight:
            if i<=allow:
                ans+=1
                allow-=i
            else:break
        return ans
            
