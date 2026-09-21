class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        hashmap = {}

        def dfs(index, cap):
            element = (index, cap)
            if index == n or cap == 0:
                return 0
            
            if element in hashmap:
                return hashmap[element]
            
            res = dfs(index + 1, cap)
            if weight[index] <= cap:
                res = max(dfs(index + 1, cap - weight[index]) + profit[index], res)
            
            final = res
            
            hashmap[element] = final
            return final


        return dfs(0, capacity)

            



