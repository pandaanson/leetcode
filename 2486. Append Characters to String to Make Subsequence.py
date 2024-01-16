class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer=0
        for char in s:
            if pointer<len(t) and char==t[pointer]:
                pointer+=1
        return len(t)-pointer
