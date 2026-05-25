class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closeOpen = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in closeOpen:
                if stack and closeOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True