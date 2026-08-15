class Solution:
    def rob(self, nums):
        # Helper function for linear House Robber (House Robber I)
        def rob_linear(houses):
            prev1 = 0  # max till previous house
            prev2 = 0  # max till house before previous
            
            for money in houses:
                temp = prev1
                prev1 = max(prev1, prev2 + money)
                prev2 = temp
            
            return prev1
        
        n = len(nums)
        
        # Edge case: only one house
        if n == 1:
            return nums[0]
        
        # Case 1: exclude last house
        case1 = rob_linear(nums[:-1])
        
        # Case 2: exclude first house
        case2 = rob_linear(nums[1:])
        
        # Return max of both cases
        return max(case1, case2)