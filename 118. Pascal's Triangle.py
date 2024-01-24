class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        ans=[[1],[1,1]]
        for i in range(2,numRows):
            temp=ans[-1]
            temp2=[]
            for j in range(1,len(temp)):
                temp2.append(temp[j]+temp[j-1])
            temp2=[1]+temp2+[1]
            ans.append(temp2)
        return ans
