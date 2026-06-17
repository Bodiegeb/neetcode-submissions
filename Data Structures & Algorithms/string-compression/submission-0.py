class Solution:
    def compress(self, chars: List[str]) -> int:
        k = 0 # writer
        n = len(chars)
        i = 0 # reader
        while i < n:
            chars[k] = chars[i]
            j = i + 1 # current char reader
            k += 1
            while j < n and chars[i] == chars[j]:
                j += 1
            
            if j - i > 1:
                for c in str(j - i):
                    chars[k] = c
                    k += 1
            i = j
        return k