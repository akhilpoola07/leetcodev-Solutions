class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        output = []
        for i,word in enumerate(words):
            if x in word:
                output.append(i)
        return output

        