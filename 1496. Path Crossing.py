class Solution:
    def isPathCrossing(self, path: str) -> bool:
        set={"0,0"}
        current=[0,0]
        for i in path:
            if i=='N':
                current[1]+=1
            elif i=='S':
                current[1]-=1
            elif i== 'E':
                current[0]+=1
            elif i=='W':
                current[0]-=1
            temp=str(current[0])+','+str(current[1])
            if temp in set:
                return True
            set.add(temp)
        return False
