class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = {}
        for c in s1:
            c1[c] = c1.get(c, 0) + 1
        for i in range(len(s2) - len(s1) + 1):
            c2 = {}
            window = s2[i:i + len(s1)]
            for c in window:
                c2[c] = c2.get(c, 0) + 1
            if c1 == c2:
                return True
        return False