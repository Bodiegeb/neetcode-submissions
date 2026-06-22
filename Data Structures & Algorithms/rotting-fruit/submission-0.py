class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        freshFruit = 0
        queue = deque()
        visited = set()
        time = 0
        for r in range(ROW):
            for c in range(COL):
                fStatus = grid[r][c]
                if fStatus == 1:
                    freshFruit += 1
                elif fStatus == 2:
                    queue.append((r,c))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue and freshFruit > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    mr = r + dr
                    mc = c + dc
                    if mr<0 or mc<0 or mr>=ROW or mc>=COL or (mr,mc) in visited or grid[mr][mc] != 1:
                        continue
                    visited.add((mr,mc))
                    queue.append((mr,mc))
                    freshFruit -= 1
            time += 1
        return time if freshFruit == 0 else -1
                



    

# grid of rotton fruit
# seems we should use level by level traversal: bc each unit of time the rot spreads by 1
# using bfs level traversal:
# edge cases: fruit not connected to main path, no rotton ones:
#   1. have a counter for the number of fresh fruit, wont search if queue is empty
# algo:
# count rotton and add to a queue
# count fresh fruit
# while both true ^
# level traverse the queue:
# add all the neighbors
# changed visited for rotton
# decrase fresh fruit counter
# increase time by 1
# if fresh fruit == 0: return time
# if not return -1