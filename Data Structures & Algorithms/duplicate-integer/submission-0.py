class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occur = {}
        for i in nums:
            if i in occur:
                return True
            else:
                occur[i] = 1

        return False