class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = min(numRows, len(s))
        if n == 1:
            return s
        else:
            list_of_strings = ["" for i in range(n)]
            direction = 1
            j = 0
            for i in range(len(s)):

                list_of_strings[j] += s[i]
                j = j + direction
                if (j+1) % n == 0 or j == 0:
                    direction = direction*(-1)

            string = ""
            string = string.join(list_of_strings)

            return string
