class Solution:
    def evalRPN(self, tokens: List[str]) -> int:       
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "/+-*":
                stack.append(int(tokens[i]))
            else:
                s2 = stack.pop()
                s1 = stack.pop()
                if tokens[i] == "+":
                    res = s1 + s2
                    stack.append(res)
                elif tokens[i] == "-":
                    res = s1 - s2
                    stack.append(res)
                elif tokens[i] == "*":
                    res = s1 * s2
                    stack.append(res)
                elif tokens[i] == "/":
                    res = int(s1 / s2)
                    stack.append(res)
                
        return stack[-1]