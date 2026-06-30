class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # Next four directions.
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])

        # Total Matrix to store total distance sum for each empty cell.
        total = [[0] * cols for _ in range(rows)]
        empty_land_value = 0
        min_dist = float('inf')

        for row in range(rows):
            for col in range(cols):
                # Start a BFS from each house.
                if grid[row][col] == 1:
                    min_dist = float('inf')

                    # Use a queue to perform a BFS, starting from the cell at (row, col).
                    q = deque([(row, col)])
                    steps = 0

                    while q:
                        steps += 1
                        level_size = len(q)

                        for level in range(level_size):
                            curr = q.popleft()

                            for dir in dirs:
                                next_row = curr[0] + dir[0]
                                next_col = curr[1] + dir[1]

                                # For each cell with the value equal to empty land value
                                # add distance and decrement the cell value by 1.
                                if (0 <= next_row < rows and
                                    0 <= next_col < cols and
                                    grid[next_row][next_col] == empty_land_value):

                                    grid[next_row][next_col] -= 1
                                    total[next_row][next_col] += steps
                                    q.append((next_row, next_col))
                                    min_dist = min(min_dist, total[next_row][next_col])

                    # Decrement empty land value to be searched in next iteration.
                    empty_land_value -= 1

        return -1 if min_dist == float('inf') else min_dist