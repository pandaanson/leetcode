class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pointer1=pointer2=0
        ls1,ls2=len(pushed),len(popped)

        stack=[]
        while pointer1<ls1:
            stack.append(pushed[pointer1])
            pointer1+=1
            while stack and stack[-1]==popped[pointer2]:
                pointer2+=1
                stack.pop()


        while pointer2<ls2:
            if stack and stack[-1]==popped[pointer2]:
                pointer2+=1
                stack.pop()
            else:
                return False
        return True

        
        
