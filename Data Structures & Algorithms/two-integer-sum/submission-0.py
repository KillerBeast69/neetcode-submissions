class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occur = {}
        for i,n in enumerate(nums):
            if target - n in occur:
                return [occur[target - n],i]

            else:
                occur[n] = i

                        
