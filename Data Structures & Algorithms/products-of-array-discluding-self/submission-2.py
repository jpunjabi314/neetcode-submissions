import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        if nums.count(0) == 1:
            index = nums.index(0)
            productatindex = math.prod(nums[:index]) * math.prod(nums[index:])
            output[index] = productatindex
            return output
        elif nums.count(0) > 1:
            return output
        else:
            product = math.prod(nums)
            for i in range(len(nums)):
                output[i] = int(product / nums[i])
            return output










        