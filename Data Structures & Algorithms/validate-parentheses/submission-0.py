class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
        }
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif s[i] in ")}]":
                if stack:
                    if pairs[s[i]] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else: 
                    return False
                    
        if not stack:
            return True
        return False