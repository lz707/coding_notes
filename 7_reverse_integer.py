class Solution:
    def reverse(self, x: int) -> int:
    *convert to string and reverse
            s = str(x)
            if abs(x) == x:
                sgn = 1
            else:
                sgn = -1
                s = s[1:]

            r = s[::-1]
            ans = int(r)*sgn
            
            if ans > 2**31-1 or ans < - 2**31:
                return 0
            else:
                return ans
        
