from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # 1. Filter out non-alphabetic characters and convert to lowercase
        target_counts = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        ans = None
        
        # 2. Iterate through each word to find valid completing words
        for word in words:
            word_counts = Counter(word)
            
            
            if all(word_counts[char] >= count for char, count in target_counts.items()):
                # Keep the shortest word (first occurrence is preserved automatically via strict '<')
                if ans is None or len(word) < len(ans):
                    ans = word
                    
        return ans