class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numdict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans=[]
        def traveller(digits,path):
            if len(digits)==0:
                ans.append(path)
            else:
                for i in numdict[digits[0]]:
                    traveller(digits[1:],path+i)
        traveller(digits,"")
        return ans
                    
