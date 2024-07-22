class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if  len(nums) < 2: return nums[0]
        i , j = 0 , len(nums)-1
        res = nums[i]^nums[j] 
        i+=1
        j -=1
        while i < j:
            res = nums[i]^nums[j] ^ res
            i+=1
            j -=1
        return  nums[i] ^  res
    # not the best the solution 
    # todo : dig about logic gates and the solution below
    # with open('user.out', 'a') as f:
    # for n in map(loads, stdin):
    #  f.write(str(reduce(xor,n))+'\n')
    # exit(0)
