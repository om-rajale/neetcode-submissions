class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i,n in enumerate(nums):
            need = target - n 
            if need in prevmap:
                return [prevmap[need],i]
            prevmap[n] = i