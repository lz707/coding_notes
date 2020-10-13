class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find all substrings, identify ones with repeating characters(set length < string length), take the max of the rest -> very time-consuming
        max_len = 0
        for i in range(len(s)-1):
            for j in range(i, len(s)+1):
                    ss = s[i:j]
                    if len(ss) == len(set(ss)) and len(ss)>max_len:
                        max_len = len(ss)
        return max_len
            
