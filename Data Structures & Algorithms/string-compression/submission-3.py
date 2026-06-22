class Solution:
    def compress(self, chars: List[str]) -> int:
        writer = 0
        reader = 0
        n = len(chars)
        while reader < n:
            chars[writer] = chars[reader]
            currChar = reader + 1
            writer += 1
            while currChar < n and chars[currChar] == chars[reader]:
                currChar += 1
            count = currChar - reader
            if count > 1:
                for c in str(count):
                    chars[writer] = c
                    writer += 1
            reader = currChar
        return writer


# GOAL: compress the number of letters in the list
# OBSERVATIONS: constant extra space "must use the chars list", can have 2+ digit numbers
# ALGO: 
# reader holds current letter, writer writes the numbers, then have currChar to extend till it gets to non reader
# if that is > 1 then write the nuber if not make the reader to currchar
#

# EX. chars = ["a","a","b","b","b","a","a","a","a","a","a"]
# ["a","2","b","3","b","a","a","a","a","a","a"]