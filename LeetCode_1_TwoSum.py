class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for b in range(0,len(nums)-1):
            for c in range(b+1,len(nums)):
                if nums[b]+nums[c]==target:
                    return (b,c)
        return (None,None)
