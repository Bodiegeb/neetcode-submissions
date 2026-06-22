class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.i = 0
        self.charCount = 0
        self.currChar = ""

    def next(self) -> str:
        if not self.hasNext():
            return ""
        if self.charCount == 0:
            self.currChar = self.s[self.i]
            self.i += 1
            while self.i < len(self.s) and self.s[self.i].isdigit():
                self.charCount = self.charCount * 10 + int(self.s[self.i])
                self.i += 1



        self.charCount -= 1
        return self.currChar

    def hasNext(self) -> bool:
        return self.charCount > 0 or self.i < len(self.s)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
