class Solution {
    public int myAtoi(String s) {
        if (s == null || s.isEmpty()) {
            return 0;
        }

        int index = 0;
        int length = s.length();

        // Step 1: Skip leading whitespace
        while (index < length && s.charAt(index) == ' ') {
            index++;
        }

        if (index == length) {
            return 0;
        }

        // Step 2: Determine sign
        int sign = 1;
        char firstChar = s.charAt(index);
        if (firstChar == '+' || firstChar == '-') {
            if (firstChar == '-') {
                sign = -1;
            }
            index++;
        }

        // Step 3 & 4: Convert digits and prevent overflow
        long accumulatedResult = 0;

        while (index < length) {
            char currentChar = s.charAt(index);

            // Stop processing if character is not a digit
            if (currentChar < '0' || currentChar > '9') {
                break;
            }

            int digit = currentChar - '0';
            accumulatedResult = accumulatedResult * 10 + digit;

            // Clamp to 32-bit signed integer limits immediately
            if (sign * accumulatedResult >= Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
            if (sign * accumulatedResult <= Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }

            index++;
        }

        return (int) (sign * accumulatedResult);
    }
}