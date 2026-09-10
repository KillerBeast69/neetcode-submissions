class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #not sure how to construct the adj list
        adj = {}
        #maybe loop through all the letterns in given list
        for i in words:
            for j in i:
                if j not in adj:
                    adj[j] = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                matched = True
                if words[i][j] != words[i + 1][j]:
                    adj[words[i][j]].add(words[i + 1][j])
                    matched = False
                    break
            if matched and len(words[i]) > len(words[i + 1]):
                return ""

            
                
            
                
        
        #now for every distinct letter there is an empty set or its neighbours
        #if only there was a visual representation of the graph, I would have known if I am doing it the right way
        
        #now I think we can run dfs on all the elements in adj
        visited = set()
        path = set()
        topsort = []
        def dfs(src, adj, visited, topsort, path):
            if src in path:
                return False
            if src in visited:
                return True
            
            visited.add(src)
            path.add(src)
            for neighbour in adj[src]:
                if dfs(neighbour, adj, visited, topsort, path) == False:
                    return False
            path.remove(src)
            topsort.append(src)
            return True

        for char in adj:
            if dfs(char, adj, visited, topsort, path) == False:
                return ""
        topsort.reverse()
        return "".join(item for item in topsort)
