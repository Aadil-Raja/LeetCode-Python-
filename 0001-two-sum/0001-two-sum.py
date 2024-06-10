class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        n=len(nums)
        for i in range(n):
            diff=target-nums[i]
            if diff in hashmap:
                return hashmap[diff],i
            hashmap[nums[i]]=i
        return
        