class Solution:
    def mySqrt(self, x: int) -> int:
        n =0 
        ans = 0   
        while ( ans < x):
            n+=1 
            ans =  ans + (n+n) - 1;            
        return n if ans <= x else n-1

        # not the best solution look for newton method
        #https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

        

        
