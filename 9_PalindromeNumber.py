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
class Solution3:
    def isPalindrome(self, x: int) -> bool:
        #Only reverse half of the number
        if x < 0 or (x%10 == 0 and x!=0):
            return False
        
        reverseNumber = 0
        while reverseNumber < x:
            reverseNumber = reverseNumber *10 + int(x % 10)
            x = int(x/10)
        

        else:
            return (reverseNumber == x or reverseNumber//10 == x)
