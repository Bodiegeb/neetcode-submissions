class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        queue.append((0,0, 1))
        visited.add((0,0))
        length = 0
        
        ROW = len(grid)
        COL = len(grid[0])
        if grid[0][0] or grid[ROW - 1][COL - 1]:
            return -1
        while queue:
            r, c, length = queue.popleft()
            if r == ROW - 1 and c == COL - 1:
                return length
            neighbors = [(0,1), (0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
            for mr, mc in neighbors:
                currRow = r + mr
                currCol = c + mc
                if currRow < 0 or currRow >= ROW or currCol < 0 or currCol >= COL or grid[currRow][currCol] != 0 or (currRow, currCol) in visited:
                    continue
                visited.add((currRow, currCol))
                queue.append((currRow, currCol, length + 1))
            length += 1
        return -1





# bfs problem
# O(n * m)
# start at starting node
# add neighbors to queue
# for each neighbor check them if it mathes bottom right
# if it doesent add those to the queue and start again