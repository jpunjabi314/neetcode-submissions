class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s[::-1]

        return s == t
        