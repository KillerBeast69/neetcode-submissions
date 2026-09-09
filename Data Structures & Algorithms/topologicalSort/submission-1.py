class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u].append(v)
    
        topsort = []
        visited = set()
        path = set()
        
        def dfs(src, adj, topsort, visited, path):
            if src in path:
                return False
            if src in visited:
                return True
            visited.add(src)
            path.add(src)
            result = None
            for neighbour in adj[src]:
                result = dfs(neighbour, adj, topsort, visited, path)
                if result == False:
                    return False                
            path.remove(src)
            topsort.append(src)

            #if there is no return statement here, then the function returns nothing  

        for i in range(n):
            result = dfs(i, adj, topsort, visited, path)
            if result == False:
                return []


        topsort.reverse()
        return topsort