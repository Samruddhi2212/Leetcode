class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Place each number x at index x - 1 if 1 <= x <= n
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its correct target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Find the first index where index + 1 doesn't match the element
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1