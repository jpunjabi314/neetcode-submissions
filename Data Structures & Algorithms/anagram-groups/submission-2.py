class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue

            group = [strs[i]]
            used[i] = True
            currentSorted = sorted(strs[i])

            for j in range(i + 1, len(strs)):
                if not used[j] and sorted(strs[j]) == currentSorted:
                    group.append(strs[j])
                    used[j] = True

            output.append(group)

        return output