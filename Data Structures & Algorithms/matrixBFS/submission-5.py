class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        visited = set()
        q = deque()

        visited.add((0, 0))
        q.append((0, 0))

        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbours = [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]

                for dr, dc in neighbours:
                    if (dr == ROWS or dc == COLS or 
                    min(dr, dc) < 0 or (dr, dc) in visited or grid[dr][dc] == 1):
                        continue
                    q.append((dr, dc))
                    visited.add((dr, dc))
            
            length += 1
        return -1
