class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastposdict={}
        lastrepeatpos=-1
        position=0
        ans=0
        for i in s:
            if i in lastposdict.keys():
                lastrepeatpos=max(lastposdict[i],lastrepeatpos)
            lastposdict[i]=position
            ans=max(ans,position-lastrepeatpos)
            position+=1
        return ans
