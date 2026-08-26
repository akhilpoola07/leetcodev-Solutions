class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""

        ans = ""
        l = 0
        ones = 0

        for r in range(len(s)):
            if s[r] == "1":
                ones += 1
            while ones == k:
                while s[l] == "0":
                    l += 1

                sub = s[l : r + 1]

              
                if (
                    not ans
                    or len(sub) < len(ans)
                    or (len(sub) == len(ans) and sub < ans)
                ):
                    ans = sub
                if s[l] == "1":
                    ones -= 1
                l += 1

        return ans