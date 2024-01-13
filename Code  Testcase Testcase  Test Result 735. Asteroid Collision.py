class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            if not stack or asteroid>0 or (stack[-1]<0 and asteroid<0):
                stack.append(asteroid)
            else:
                while stack and abs(stack[-1])<abs(asteroid) and stack[-1]>0:
                    stack.pop()
                if stack and abs(stack[-1])==abs(asteroid) and stack[-1]>0:
                    stack.pop()
                elif not stack or stack[-1]<0:
                    stack.append(asteroid)
        return stack
        
