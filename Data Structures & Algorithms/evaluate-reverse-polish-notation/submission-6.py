class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                num2, num1 = stack.pop(), stack.pop()
                match c:
                    case '+':
                        stack.append(num1 + num2)
                    case '*':
                        stack.append(num1 * num2)
                    case '-':
                        stack.append(num1 - num2)
                    case '/':
                        stack.append(int(num1 / num2))
        return stack[0]


        