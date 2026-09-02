class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        missing = []
        for i, count in enumerate(nums):
            if count > 0:
                missing.append(i + 1)
                
        return missing