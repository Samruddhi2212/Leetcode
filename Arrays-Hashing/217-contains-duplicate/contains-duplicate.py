class Solution:
    def containsDuplicate(self, nums) :
        top = set()
        for n in nums:
            if n in top:
                return True
            top.add(n)
        return False