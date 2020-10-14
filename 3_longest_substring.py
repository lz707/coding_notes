class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find all substrings, identify ones with repeating characters(set length < string length), take the max of the rest -> very time-consuming
        max_len = 0
        for i in range(len(s)-1):
            for j in range(i, len(s)+1):
                    ss = s[i:j]
                    if len(ss) == len(set(ss)) and len(ss)>max_len:
                        max_len = len(ss)
        return max_len
            
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window substring[i:j], increase j by 1 and check if the new character is in the current substring. 
        #If there is duplication, find index of the duplicate character t and start next loop with t+1. Keep j intact as j does not need to go backwards.
        
        max_len = 0
        i = 0
        j = 1
        while i <= j <= len(s):
            max_len = max(max_len, len(s[i:j]))
            if s[j:j+1] in s[i:j]:
                i = i + s[i:j].index(s[j:j+1]) + 1  
            else:
                j = j + 1           
        return max_len
    
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a list and append each character in order. If encounter duplication, find index of first occurence and start list one position after that
        
        str_list = []
        max_len = 0
        
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]
                    
            str_list.append(x)
            max_len = max(max_len, len(str_list))
        return max_len
