class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        para = []
        def backtrack(opened, closed):
            # When to add to the list
            if opened == closed == n:
                res.append("".join(para))
                return
            # explore open
            if opened < n:
                para.append("(")
                backtrack(opened + 1, closed)
                para.pop()
            # exlpre closeing ones
            if closed < opened:
                para.append(")")
                backtrack(opened, closed + 1)
                para.pop()

        backtrack(0 , 0)
        return res