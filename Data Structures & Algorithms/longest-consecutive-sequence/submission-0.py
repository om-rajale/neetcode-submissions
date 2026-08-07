class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        longest = 0
        for n in numsset:
            if n-1 not in numsset:
                length = 1
                current = n
                while current+1 in numsset:
                    length+=1
                    current+=1
                longest = max(longest,length)
        return longest
