class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Sset = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in Sset:
                Sset.remove(s[left])
                left+=1
            Sset.add(s[right])
            res = max(res,right-left+1)
        return res