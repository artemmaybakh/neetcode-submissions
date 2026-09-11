class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        s = s.lower()
        for i in range(len(s)):
            if 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57:
                a.append(s[i])
        if a == a[::-1]:
            return True

        return False