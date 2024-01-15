class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        eqrelation=[[] for _ in range(26)]
        uneqreplation=[]
        visited=[False for _ in range(26)]
        for equation in equations:
            if equation[1]=='!':
                uneqreplation.append([ord(equation[0]) - ord('a'),ord(equation[3]) - ord('a')])

            else:
                eqrelation[ord(equation[0]) - ord('a')].append(ord(equation[3]) - ord('a'))
                eqrelation[ord(equation[3]) - ord('a')].append(ord(equation[0]) - ord('a'))

        tempgroup=0
        group=[-1 for _ in range(26)]
        for i in range(26):
            if not visited[i]:
                stack=[i]
                while stack:
                    temp=stack.pop()
                    group[temp]=tempgroup
                    visited[temp]=True
                    while eqrelation[temp]:
                        stack.append(eqrelation[temp].pop())
                tempgroup+=1

        for i,j in uneqreplation:
            if group[i]==group[j]:
                return group[i]<0
        return True
