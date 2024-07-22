class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNums = {}
        for i , n in enumerate(nums):
            if ( target - n)   in mapNums: return { i , mapNums[target - n ]}
            else: mapNums[n]=i
