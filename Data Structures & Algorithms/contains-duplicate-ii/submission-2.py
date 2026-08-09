class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for left in range(len(nums)):
            for right in range(left+1,len(nums)):
                if nums[left] == nums[right] and right-left <=k:
                    return True
        return False
