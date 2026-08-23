class Solution:
    def intToRoman(self, num: int) -> str:
        # Predefined mappings ordered from largest to smallest value
        val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
            (1, "I")
        ]
        
        roman_parts = []
        for val, symbol in val_map:
            if num == 0:
                break
            
            # Determine how many times the symbol fits into num
            count = num // val
            if count > 0:
                roman_parts.append(symbol * count)
                num %= val
                
        return "".join(roman_parts)