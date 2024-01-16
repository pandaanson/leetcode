class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        for i in costs:
            if i<=coins:
                coins-=i
                ans+=1
            else:
                return ans
        return ans
