class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s.reverse() == t:
            return True
        else:
            return False