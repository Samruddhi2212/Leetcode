class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # no point continuing, sorted array
                path.append(candidates[i])
                # same index i (not i+1) since we can reuse the same number
                backtrack(i, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
    # [[2,2,3],[7]]
    print(sol.combinationSum([2, 3, 5], 8))
    # [[2,2,2,2],[2,3,3],[3,5]]