from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        output = []

        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = 0
            
            dictionary[nums[i]] += 1
        
        for i in range(k):
            greatest = max(dictionary, key=dictionary.get)
            output.append(greatest)
            del dictionary[greatest]

        return output





        """
        results = [0] * k
        result = dict(Counter(nums))

        for i in (range(result.count())):
            results[i - 1] = result.get(item, 0) + 1
        
        return results
        """


        