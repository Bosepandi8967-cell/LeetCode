class Solution:
    def calculate(self, s: str) -> int:
        total, last_num, current_num = 0, 0, 0
        operator = '+' 
        for i, char in enumerate(s + '+'): 
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char != ' ':
                if operator == '+':
                    total += last_num
                    last_num = current_num
                elif operator == '-':
                    total += last_num
                    last_num = -current_num
                elif operator == '*':
                    last_num = last_num * current_num
                elif operator == '/':
                    last_num = int(last_num / current_num) 
                operator = char
                current_num = 0
        return total + last_num
