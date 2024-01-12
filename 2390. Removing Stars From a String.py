class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for i in s:
            if i=='*':
                ans.pop()
            else:
                ans.append(i)
        return ''.join(ans)

# Given a string 's' that includes asterisks '*'.
# In each operation, the following steps are performed:
# 1. Select an asterisk in 's'.
# 2. Eliminate the nearest character to the left of the asterisk that is not an asterisk, and then remove the asterisk itself.
# The task is to return the string after all asterisks have been processed and removed.
# Additional Notes:
# - The input string is constructed in a way that ensures the operation can always be executed.
# - It is guaranteed that the final string after all operations will be uniquely determined.

