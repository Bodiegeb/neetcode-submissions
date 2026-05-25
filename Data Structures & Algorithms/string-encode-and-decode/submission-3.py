class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedS = ""
        for word in strs:
            encodedS += str(len(word)) + "#" + word
        return encodedS

    def decode(self, s: str) -> List[str]:
        decodedS = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = str(s[j + 1: j + 1 + length])
            decodedS.append(word)
            i = j + 1 + length
        return decodedS