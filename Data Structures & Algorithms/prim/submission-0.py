class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for i in range(n):
            adj[i] = []

        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        minheap = []
        for neighbour, weight in adj[0]:
            heapq.heappush(minheap, [weight, 0, neighbour])

        total = 0
        visited = set()

        visited.add(0)
        while minheap:
            weight, n1, n2 = heapq.heappop(minheap)
            
            if n2 in visited:
                continue
            total += weight
            visited.add(n2)
            for neighbour, weight in adj[n2]:
                if neighbour not in visited:
                    heapq.heappush(minheap, [weight, n2, neighbour])
        return total
             