class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for key,val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff],key]
            prevMap[val] = key
        return 