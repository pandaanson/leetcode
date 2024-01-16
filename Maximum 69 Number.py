class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        ln=len(num)
        for i in range(ln):
            if num[i]=='6':
                ans=''
                if i>0:
                    ans+=num[:i]
                ans+='9'
                if i<ln-1:
                    ans+=num[i+1:]
                return int(ans)
        return int(num)
