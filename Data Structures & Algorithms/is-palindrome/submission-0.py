class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = [c.lower() for c in s if c.isalnum()]
        return s_cleaned == list(reversed(s_cleaned))