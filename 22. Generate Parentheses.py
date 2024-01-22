class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(currenthist, leftcount, rightcount):
            if leftcount > rightcount:  # Ensure that the parentheses are well-formed
                return
            if leftcount == 0 and rightcount == 0:
                ans.append(currenthist)
                return
            if leftcount > 0:
                helper(currenthist + '(', leftcount - 1, rightcount)
            if rightcount > 0:
                helper(currenthist + ')', leftcount, rightcount - 1)

        helper('', n, n)
        return ans
