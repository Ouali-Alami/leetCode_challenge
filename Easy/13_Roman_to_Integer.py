class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = len(s) - 1
        ans = romanNum[s[i]]
        while i > 0:
            nextNum = romanNum[s[i - 1]];
            if romanNum[s[i]] <= nextNum :
                ans = ans + nextNum
            else:
                ans = ans - nextNum
            i = i - 1
        return ans

    # not the best way
    # like with the databases requests its better to compare directly with the values...
    # u can directly substract the numbers related to the terms below:
    # I can be placed before V (5) and X (10) to make 4 and 9. 
    # X can be placed before L (50) and C (100) to make 40 and 90. 
    # C can be placed before D (500) and M (1000) to make 400 and 900.
