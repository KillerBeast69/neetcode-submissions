class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def helper(grid, r, c, visited):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                grid[r][c] == 1 or (r, c) in visited):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visited.add((r, c))

            count = 0
            count += helper(grid, r + 1, c, visited)
            count += helper(grid, r - 1, c, visited)
            count += helper(grid, r, c + 1, visited)
            count += helper(grid, r, c - 1, visited)

            visited.remove((r, c))

            return count


        return helper(grid, 0, 0, set())