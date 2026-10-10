import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        output = [0] * len(nums)
        tempproduct = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                tempproduct = product / nums[i]
            else:
                tempproduct = 0
            
            output[i] = int(tempproduct)
    
        return output





        