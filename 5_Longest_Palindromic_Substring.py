class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand around center. decide substring with center and length. There are two scenarios: center is one character or between two characters.
        # Note: get the start & end right
        
        def expandCenter(string, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1

            return r - l - 1
        
        start = 0
        end = 0
      
        for i in range(len(s)):
            len1 = expandCenter(s, i, i)
            len2 = expandCenter(s, i, i+1)
            long_len = max(len1, len2)
            if long_len > end - start:
                start = i - (long_len - 1) // 2
                end = i + long_len // 2 + 1
        
        return s[start:end]
