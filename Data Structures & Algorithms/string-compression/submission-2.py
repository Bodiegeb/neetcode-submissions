class Solution:
    def compress(self, chars: List[str]) -> int:
        writer = 0
        reader = 0
        while reader < len(chars):
            chars[writer] = chars[reader]
            currChar = reader + 1
            writer += 1
            while currChar < len(chars) and chars[currChar] == chars[reader]:
                currChar += 1

            if currChar - reader > 1:
                for c in str(currChar - reader):
                    chars[writer] = c
                    writer += 1
            reader = currChar
        return writer



# GOAL: compress the number of letters in the list
# OBSERVATIONS: constant extra space "must use the chars list", can have 2+ digit numbers
# ALGO: 
# i will keep track of the current spot, then use j to find the curr char how many of the currChars there are
# update: then update with i, get the count and change it to a string then go through each number and add to list
# jump to j and start again

# EX. chars = ["a","a","b","b","b","a","a","a","a","a","a"]
# ["a","2","b","3","b","a","a","a","a","a","a"]