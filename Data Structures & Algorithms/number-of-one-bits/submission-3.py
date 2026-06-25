class Solution:
    def hammingWeight(self, n: int) -> int:
        num = str(bin(n))
        res = 0
        for i in range(len(num)):
            if num[i] == "1":
                res += 1
        return res