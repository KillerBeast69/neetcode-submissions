class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid)
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in neighbours:
                    R = dr + r
                    C = dc + c
                    if (min (R, C) < 0 or R >= ROWS or C >= COLS or 
                        (R, C) in visited or grid[R][C] == 1):
                        continue
                    queue.append((R, C))
                    visited.add((R,C))

            length += 1
        return -1
