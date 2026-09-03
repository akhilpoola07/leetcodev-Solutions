class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_val = min(nums1)
        
        # If min_val is odd, we can make all elements odd.
        if min_val % 2 != 0:
            return True
            
        # If min_val is even, we can only make all elements even if there are NO odd numbers at all.
        return all(x % 2 == 0 for x in nums1)