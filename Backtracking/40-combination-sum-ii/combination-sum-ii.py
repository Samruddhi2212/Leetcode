class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # sorted array, no point continuing
                # skip duplicates at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])  # i+1: no reuse
                path.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(sol.combinationSum2([2, 5, 2, 1, 2], 5))
    # [[1,2,2],[5]]