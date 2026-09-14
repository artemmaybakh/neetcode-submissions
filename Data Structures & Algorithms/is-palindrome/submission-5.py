class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        s = s.lower()

        for i in range(len(s)):
            #print(s[i])
            if 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57:
                a.append(s[i])
        j = -1
        print(a)
        for i in range(len(a) // 2):
            if a[i] != a[j]:
                return False
            j -= 1

        return True