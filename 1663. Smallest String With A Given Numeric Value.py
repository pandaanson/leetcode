class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans=['a' for _ in range(n)]
        k-=n
        for i in range(n-1,-1,-1):
            if k>=25:
                k-=25
                ans[i]='z'
            elif k>0:
                ans[i]=chr(k + 97)
                return ''.join(ans)
            else:
                return ''.join(ans)
        return ''.join(ans)
        
