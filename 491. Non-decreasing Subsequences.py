class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(start_index, path):
            if len(path) >= 2:
                ans.add(tuple(path))  # Add the subsequence as a tuple to the set

            for i in range(start_index, len(nums)):
                # Only add the number if it's greater than or equal to the last number in the path
                if not path or nums[i] >= path[-1]:
                    dfs(i + 1, path + [nums[i]])

        ans = set()
        dfs(0, [])
        return list(map(list, ans))  # Convert each tuple back to a list
