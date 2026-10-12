class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums) - 2):             
            target = nums[i]
            if i > 0 and target == nums[i - 1]:
                continue                              

            l = i + 1                                
            r = len(nums) - 1

            while l < r:
                if (-1 * (nums[l] + nums[r])) == target:
                    output.append([target, nums[l], nums[r]])
                    l += 1                          
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1                         
                else:
                    if (-1 * (nums[l] + nums[r])) > target:
                        l += 1
                    else:
                        r -= 1

        return output