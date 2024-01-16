from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts= Counter(arr)
        counts = sorted(counts.values(), reverse = True)
        n = 0
        ans = 0
        la=len(arr)
        # Remove numbers until at least half are removed.
        for count in counts:
            n += count
            ans += 1
            if (n >= la//2):
                break

        return ans
