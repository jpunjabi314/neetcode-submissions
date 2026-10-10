class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            current1 = nums[i]
            for j in range(1, len(nums)):
                current2 = nums[j]
                for k in range(2, len(nums)):
                    current3 = nums[k]
                    if current1 + current2 + current3 == 0 and i != j and i != k and j != k:
                        temp = [current1, current2, current3]
                        temp.sort()
                        if temp not in output:
                            output.append(temp)
                        temp = []
        

        return output

                    

