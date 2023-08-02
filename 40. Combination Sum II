class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, index, path):
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target-candidates[i], i+1, path+[candidates[i]])

        candidates.sort()
        res = []
        dfs(target, 0, [])
        return res
