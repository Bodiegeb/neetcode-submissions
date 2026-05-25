class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closeOpen = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in closeOpen:
                if stack and closeOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
            