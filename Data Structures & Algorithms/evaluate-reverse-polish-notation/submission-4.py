class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(num1 + num2)
                elif c == "*":
                    stack.append(num1 * num2)
                elif c == "-":
                    stack.append(num1 - num2)
                elif c == "/":
                    stack.append(int(num1 / num2))
        return stack[0] if stack else None
