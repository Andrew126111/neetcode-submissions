class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c.isdigit() or (len(c) > 1 and c[0] == '-'):
                stack.append(int(c))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if c == '+': stack.append(op1 + op2)
                elif c == '-': stack.append(op1 - op2)
                elif c == '*': stack.append(op1 * op2)
                else: stack.append(int(op1 / op2))
        return stack[0]