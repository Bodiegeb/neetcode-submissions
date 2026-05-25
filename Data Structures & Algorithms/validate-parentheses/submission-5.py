class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closed = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in closed:
                if stack and closed[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
            