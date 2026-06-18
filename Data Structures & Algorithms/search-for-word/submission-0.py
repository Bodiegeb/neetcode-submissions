class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visted = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROW or c >= COL or board[r][c] != word[i] or (r, c) in visted:
                return False
            visted.add((r, c))
            res = dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1)
            visted.remove((r, c))
            return res
        for row in range(ROW):
            for col in range(COL):
                if dfs(row, col, 0):
                    return True
        return False


