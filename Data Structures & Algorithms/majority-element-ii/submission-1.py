class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
            if count[num]> len(nums)/3:
                res.add(num)
        return list(res)