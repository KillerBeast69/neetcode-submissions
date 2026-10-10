class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        
        total = 0
        for i, j in hashmap.items():
            if j == 1:
                return -1
            if j % 3 == 0:
                total += j // 3
            if j % 2 == 0:
                total += j // 2

        return total
            
        
