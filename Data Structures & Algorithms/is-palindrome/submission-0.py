class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                st+=i
        if st == st[::-1]:
            return True

        return False