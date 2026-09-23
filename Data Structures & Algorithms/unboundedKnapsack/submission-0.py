class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, C = len(profit), capacity
        DP = [0] * (C + 1)

        for i in range(N):
            cur = [0] * (C + 1)
            for c in range(1, C + 1):
                skip = DP[c]
                include = 0

                if c - weight[i] >= 0:
                    include = profit[i] + cur[c - weight[i]]
                cur[c] = max(include, skip)
            DP = cur
        return DP[C]
         