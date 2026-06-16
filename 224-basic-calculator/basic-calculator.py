class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, num, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c) 
            elif c == "+":
                res += sign * num       
                num, sign = 0, 1        
            elif c == "-":
                res += sign * num       
                num, sign = 0, -1       
            elif c == "(":
                stack.append(res)       
                stack.append(sign)      
                res, sign = 0, 1        
            elif c == ")":
                res += sign * num       
                num = 0
                res *= stack.pop()      
                res += stack.pop()      
        return res + (sign * num)       
