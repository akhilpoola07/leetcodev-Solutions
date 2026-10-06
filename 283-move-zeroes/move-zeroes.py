class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = 0
        for l in range(len(nums)):
            if nums[l] != 0:
                nums[k],nums[l] = nums[l],nums[k]
                k+=1 