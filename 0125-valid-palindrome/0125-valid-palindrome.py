class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(e for e in s if e.isalnum()).lower()
        
        if s == s[::-1]:
            return True
        else:
            return False