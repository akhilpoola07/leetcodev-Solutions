class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        su = []
        for row in matrix:
            su.append(sum(row))
        return su