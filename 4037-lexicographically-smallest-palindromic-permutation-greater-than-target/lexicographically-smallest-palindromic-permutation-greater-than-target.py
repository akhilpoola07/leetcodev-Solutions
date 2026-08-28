from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Check if a valid palindromic permutation is possible
        odd_chars = [ch for ch, count in counts.items() if count % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Available character pool for the first half
        half_counts = {ch: count // 2 for ch, count in counts.items() if count // 2 > 0}
        
        m = n // 2
        
        # Helper to construct the smallest palindrome given the prefix of the first half
        def build_palindrome(prefix_half, remaining_counts):
            first_half = list(prefix_half)
            for ch in sorted(remaining_counts.keys()):
                first_half.extend([ch] * remaining_counts[ch])
            first_half_str = "".join(first_half)
            
            if n % 2 == 1:
                return first_half_str + mid_char + first_half_str[::-1]
            else:
                return first_half_str + first_half_str[::-1]

        # Try to match a prefix of target's first half of length `i`
        for i in range(m, -1, -1):
            prefix = target[:i]
            
            # Check if target[:i] can be formed from half_counts
            temp_counts = half_counts.copy()
            valid_prefix = True
            for ch in prefix:
                if temp_counts.get(ch, 0) > 0:
                    temp_counts[ch] -= 1
                    if temp_counts[ch] == 0:
                        del temp_counts[ch]
                else:
                    valid_prefix = False
                    break
            
            if not valid_prefix:
                continue
            
            # If we matched all m positions of the first half
            if i == m:
                candidate = build_palindrome(prefix, temp_counts)
                if candidate > target:
                    return candidate
                continue
            
            # Otherwise, pick a character strictly larger than target[i] at position i
            target_char = target[i]
            available_chars = sorted([ch for ch in temp_counts if ch > target_char])
            
            for next_char in available_chars:
                next_counts = temp_counts.copy()
                next_counts[next_char] -= 1
                if next_counts[next_char] == 0:
                    del next_counts[next_char]
                
                candidate = build_palindrome(prefix + next_char, next_counts)
                if candidate > target:
                    return candidate
        
        return ""