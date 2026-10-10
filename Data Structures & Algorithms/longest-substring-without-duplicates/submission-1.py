class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        count = 0
        tempList = []
        
        for letter in s:
            if letter not in tempList:
                tempList.append(letter)
                count += 1
                best = max(count, best)
            else:
                tempList = []
                count = 1
                tempList.append(letter)
        
        return best
        