class Solution1:
    def isPalindrome(self, x: int) -> bool:
        #convert to string
        x = str(x)
        ans = True
        for i in range(len(x)):
            if x[i] == x[-i-1]:
                continue
            else:
                ans = False
                break
        return ans



class Solution2:
    def isPalindrome(self, x: int) -> bool:
        #NOT converting to string. 
        num_list = []
        while x >= 1:
            num = x % 10
            num_list.append(num)
            x = int(x/10)
        ans = True
        for i in range(len(num_list)):
            if num_list[i] == num_list[-i-1]:
                continue
            else:
                ans = False
                break
        if x < 0:
            return False
        else:
            return ans
