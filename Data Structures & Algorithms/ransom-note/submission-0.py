class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterset = defaultdict(int)
        for letter in magazine:
            letterset[letter] += 1
        
        for letter in ransomNote:
            if letterset[letter] <= 0:
                return False
            letterset[letter] -= 1
        return True