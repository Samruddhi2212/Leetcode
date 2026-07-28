class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first: bool) -> int:
            low, high = 0, len(nums) - 1
            bound = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        high = mid - 1  # Keep searching left
                    else:
                        low = mid + 1   # Keep searching right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return bound

        return [find_bound(True), find_bound(False)]