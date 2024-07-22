 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        if x < 10 : return True
        nbDigits = math.floor(log10(x))
        divider = math.pow(10, nbDigits)
        nb =x
        while(nb) :
            # we compare left and right
            if nb // divider  !=  nb%10: return False
            # then we drop off left and right digit ()
            nb = (nb% divider) // 10
            # then we decrement the divider by 2 digits
            divider = divider * math.pow(10, -2)
        return True

        # better solution below we move like two pointers on from left the other from right and 
        # before they arrived in the same digit( the middle of the number) we stop 
        # and look if half number left equals to half number right 
        # the case of x == result // 10 id for the odd number of digits  

        # result = 0

        #while x > result:
        #    result = result * 10 + x % 10
        #    x = x // 10	
        
        #return True if (x == result or x == result // 10) else False

            
