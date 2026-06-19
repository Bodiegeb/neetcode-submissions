class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        para = []
        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(para))
                return
            # explore open para
            if opened < n:
                para.append("(")
                backtrack(opened + 1, closed)
                para.pop()
            # explore closed para
            if closed < opened:
                para.append(")")
                backtrack(opened, closed + 1)
                para.pop()
        backtrack(0, 0)
        return res



# Valid sets of para
#      []
#    ["("] [")"] 
# ["(("] ["()""]

# base case equal number of open and closed para
# explore either adding a ( or )