class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        under=[[] for _ in range(n)]
        for i in range(n):
            if manager[i]!=-1:
                under[manager[i]].append(i)
        stack=[[headID,0]]
        print(under)
        ans=0
        while stack:
            temp=stack.pop()
            if under[temp[0]]:
                for i in under[temp[0]]:
                    stack.append([i,informTime[temp[0]]+temp[1]])
            else:
                ans=max(ans,temp[1])

        return ans
