import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        output = [0] * len(nums)
        tempproduct = 0

        for i in range(len(nums)):
            result = math.prod(nums[0:i]) * math.prod(nums[i+1:len(nums)])
            output[i] = int(result)

        return output





        