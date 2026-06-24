class Solution:
    def compress(self, chars: List[str]) -> int:
        reader = 0
        writer = 0
        n = len(chars)
        while reader < n:
            chars[writer ] = chars[reader]
            writer += 1
            currChar = reader + 1
            while currChar < n and chars[currChar] == chars[reader]:
                currChar += 1
            # this is once they find the end of the list
            if currChar - reader > 1:
                for c in str(currChar - reader):
                    chars[writer] = c
                    writer += 1
            reader = currChar
        return writer


#GOAL: compress the number of string letters in a list without extra space

# OB: only write if the length of letters if > 1
# - can be larger than 10 and must be split
# - needs O(1) extra space so i need to just use the chars list

# IDEAS: - have a reader that reads the current letter, a writer that writes the length, 
# curr letter that goes through the list

# ["a","4","b","a","b","b","b","b","a","a","a"]
#           ^        ^  ^      

# 
# reader reads curr letter and writer writes
# move writer down and create currletter
#  move curr letter until its not on reader lettter and keep count
# writer then writers teh number in the a
# reader moves to currletter


