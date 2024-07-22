class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) -1
        while i > -1 and digits[i] == 9:
            digits[i]= 0
            i -= 1
        if i < 0:
            return [1] + digits
        else:
             digits[i]= digits[i] + 1
        return digits
