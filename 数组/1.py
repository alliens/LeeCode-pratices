''''
时间超限
class Solution:
    def twoSum(self,nums,target):
        for i in range(nums):
            for j in range(nums):
                if nums[i]+nums[j]==target and i!=j:
                    return[i,j]
'''
#法1:暴力解法
'''
class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j
'''

#法2:
class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            if target-nums[i] in nums[i:]:
                return [i,nums.index(target-nums[i],i+1)]

