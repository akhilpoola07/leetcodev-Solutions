from collections import defaultdict

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        counts = defaultdict(int)
        pairs = 0
        
        for a, b in dominoes:
           
            key = tuple(sorted((a, b)))
            
            pairs += counts[key]
            counts[key] += 1
            
        return pairs